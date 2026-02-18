import streamlit as st
from src.visualize import plot_warehouse
from src.orders import process_order
from src.warehouse import Warehouse
from src.optimizer import optimize_route, total_distance, naive_route

# MUST be first Streamlit command
st.set_page_config(page_title="Warehouse Picking Optimizer", layout="wide")

st.title("📦 Warehouse Picking Optimizer")

# ---------------- MODE SELECTION ----------------
st.subheader("Order Input Method")

mode = st.radio(
    "Choose how you want to enter the order:",
    ["Natural Language (AI Assisted)", "Manual Selection (No AI)"]
)

# ---------------- SHOW INVENTORY ----------------
warehouse_preview = Warehouse()

st.subheader("🧾 Available Products in Warehouse")

product_cols = st.columns(3)
products = list(warehouse_preview.products.keys())

for i, item in enumerate(products):
    product_cols[i % 3].info(item)

# ---------------- HOW TO USE ----------------
with st.expander("How to use this tool"):
    st.write("""
    1. Type the items you want in natural language OR manually select them.
    2. You can mark priority items using the word 'urgent'.
    3. Adjust cart capacity to simulate worker trolley size.
    4. Click 'Optimize Route' to see the picking path.
    """)

# ---------------- AI MODE INPUT ----------------
manual_items = []
manual_urgent = []

if mode == "Natural Language (AI Assisted)":

    st.write("Describe the items needed in natural language.")
    st.write("You can mark priority items using the word **urgent**.")

    # Example buttons
    colE1, colE2 = st.columns(2)

    if colE1.button("Load Example Order"):
        st.session_state["example_text"] = """urgent: charger and notebook
also get a mouse and a water bottle"""

    if colE2.button("Clear"):
        st.session_state["example_text"] = ""

    if "example_text" not in st.session_state:
        st.session_state["example_text"] = ""

    user_input = st.text_area(
        "Order description:",
        value=st.session_state["example_text"],
        height=150
    )

else:
    # ---------------- MANUAL MODE INPUT ----------------
    st.subheader("Select Required Items")

    manual_items = st.multiselect(
        "Choose products from warehouse inventory:",
        products
    )

    manual_urgent = st.multiselect(
        "Mark urgent items:",
        manual_items
    )

    user_input = ""  # no text needed

# ---------------- CAPACITY ----------------
capacity = st.slider("Cart Capacity (max items per trip)", 1, 6, 3)

# ---------------- BUTTON ACTION ----------------
if st.button("Optimize Route"):

    with st.spinner("Calculating optimal picking route..."):

        warehouse = Warehouse()
        entrance = (0, 0)

        # ---- ORDER PROCESSING DEPENDING ON MODE ----
        if mode == "Natural Language (AI Assisted)":
            urgent_items, normal_items = process_order(user_input)
        else:
            urgent_items = manual_urgent
            normal_items = [i for i in manual_items if i not in manual_urgent]

        items = urgent_items + normal_items

        if not items:
            st.error("No items selected or detected.")
            st.stop()

        # ---- DISPLAY DETECTED ITEMS ----
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🚨 Urgent Items")
            if urgent_items:
                for item in urgent_items:
                    st.success(item)
            else:
                st.write("None")

        with col2:
            st.subheader("📋 Normal Items")
            if normal_items:
                for item in normal_items:
                    st.info(item)
            else:
                st.write("None")

        # ---- LOCATIONS ----
        urgent_locations = [warehouse.get_location(i) for i in urgent_items if warehouse.get_location(i)]
        normal_locations = [warehouse.get_location(i) for i in normal_items if warehouse.get_location(i)]

        # ---- BASELINE (NO OPTIMIZATION, SAME CAPACITY) ----
        baseline_route = [entrance]
        remaining_baseline = (urgent_locations + normal_locations).copy()

        while remaining_baseline:
            batch = remaining_baseline[:capacity]
            remaining_baseline = remaining_baseline[capacity:]

            for loc in batch:
                baseline_route.append(loc)

            baseline_route.append(entrance)

        baseline_distance = total_distance(baseline_route)

        # ---- OPTIMIZED ROUTE ----
        all_locations = (urgent_locations + normal_locations)

        route = [entrance]
        remaining = all_locations.copy()

        while remaining:
            batch = remaining[:capacity]
            remaining = remaining[capacity:]

            trip_route = optimize_route(entrance, batch)
            route += trip_route[1:]
            route.append(entrance)

        distance = total_distance(route)

        # ---- PERFORMANCE ----
        st.subheader("📊 Performance Improvement")

        saved = baseline_distance - distance
        percent = (saved / baseline_distance * 100) if baseline_distance > 0 else 0

        colA, colB, colC = st.columns(3)
        colA.metric("Normal Worker Distance", f"{baseline_distance} units")
        colB.metric("Optimized Distance", f"{distance} units")
        colC.metric("Distance Saved", f"{saved} units", f"{percent:.1f}% improvement")

        # ---- INSTRUCTIONS ----
        st.subheader("👷 Worker Instructions")

        trip = 1
        st.write(f"Trip {trip}: Start at entrance")

        for i in range(1, len(route)):
            step = route[i]
            if step == entrance:
                st.write("Return to entrance and unload items")
                trip += 1
                if i != len(route) - 1:
                    st.write(f"Trip {trip}: Continue picking")
            else:
                st.write(f"Go to shelf {step} and pick item")

        # ---- MAP ----
        st.subheader("🗺️ Warehouse Route Map")
        fig = plot_warehouse(route, warehouse.products)
        st.pyplot(fig)
