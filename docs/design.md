Warehouse Picking Optimizer – Technical Documentation

1. System Purpose

The Warehouse Picking Optimizer is a decision-support system designed to minimize walking distance during order picking in a warehouse.
The system simulates a fulfillment environment and computes an efficient picking sequence for a worker based on product locations.

The application demonstrates how algorithmic optimization and AI-assisted processing can improve operational efficiency in logistics.

2. System Architecture

The system is divided into independent modules:

Module	Responsibility
warehouse.py	Stores product locations
optimizer.py	Computes optimal route
ai_parser.py	Interprets user order
visualize.py	Displays warehouse path
instruction_generator.py	Generates worker guidance
main.py	Coordinates system workflow

The architecture follows a modular design, meaning each component performs a single responsibility and can be modified independently.

3. Warehouse Model

The warehouse is modeled as a 2D grid:

Each product has a fixed coordinate (x, y)

Entrance is located at (0,0)

Coordinates represent shelf locations

Example:

toothpaste → (2,8)
mouse → (3,4)
notebook → (5,1)


This abstraction simulates real warehouse shelving without requiring physical sensors.

4. Order Interpretation

The user enters a natural language request.

Example:

"I need a bottle and a notebook"


The system uses semantic similarity matching to map user language to known inventory items.

Steps:

Sentence embedding is generated

Each product name is embedded

Cosine similarity is calculated

Closest matching items are selected

This allows flexible user input instead of exact product typing.

5. Route Optimization Algorithm
Problem Type

The picking problem is a variation of the Travelling Salesman Problem (TSP).

Goal:
Find a path visiting all required item locations with minimal distance.

Selected Solution

The project uses the Nearest Neighbor Heuristic.

Algorithm:

Start at entrance

Find nearest unvisited item

Move to that item

Repeat until all items are collected

Why Nearest Neighbor?

Fast computation

Works well for moderate number of items

Simple to implement

Suitable for real-time picking decisions

6. Distance Metric

The system uses Manhattan Distance:

distance = |x1 - x2| + |y1 - y2|


Reason:
Warehouse workers move along aisles and rows, not diagonally.

Therefore Manhattan distance better represents real walking effort.

7. Visualization

The path is visualized using matplotlib.

Displayed elements:

product locations

labels

worker path

entrance

This helps verify optimization correctness and provides intuitive understanding of the route.

8. AI Integration (ScaleDown)

The ScaleDown API is integrated for AI-assisted instruction optimization.

Role of AI:

Improve clarity of worker instructions

Convert route information into human-readable guidance

The AI does not perform optimization.
The optimization logic remains algorithmic to ensure reliability and reproducibility.

9. Instruction Generation

After route calculation:

Route coordinates are generated

Step sequence is created

AI-assisted formatting produces readable worker instructions

Example:

Start at entrance
Proceed to shelf (5,1)
Pick item
Continue to next location

10. Workflow Sequence

User enters order

System interprets items

Item coordinates retrieved

Optimized path computed

Distance calculated

Visualization generated

Instructions displayed

11. Design Decisions
Why algorithmic optimization instead of full AI routing?

AI models are non-deterministic and unreliable for path planning.
Optimization algorithms guarantee predictable and efficient routes.

Why modular design?

Easier debugging

Easier extension

Clear separation of concerns

Why local processing for item detection?

Ensures system works offline and avoids API dependency for core functionality.

12. Limitations

Assumes static product locations

Single worker only

No real-time obstacle handling

No inventory stock tracking

13. Possible Enhancements

Multi-worker route coordination

Real warehouse map import

Dynamic order batching

Mobile interface

Real-time inventory updates

Collision avoidance

14. Conclusion

The system demonstrates a practical application of computer science concepts in logistics operations.
It combines optimization algorithms with AI-assisted human interaction to simulate an industrial warehouse support tool.

The project emphasizes reliability, efficiency, and usability rather than conversational AI, reflecting real-world engineering systems.