# -Galactic-Cargo-Management-System

🌌 Overview

In the vast expanse of interstellar trade, cargo management is a mission-critical problem. Each spaceship carries bins of different capacities, and shipments come in varying sizes with special handling requirements. Inefficient placement of cargo can lead to wasted space, delays, and increased costs.

The Galactic Cargo Management System (GCMS) is a project designed to solve this by providing an efficient cargo allocation system. It uses advanced algorithms to pack objects into bins based on their color-coded handling instructions:

Blue Cargo → Compact Fit, choose bin with least ID

Yellow Cargo → Compact Fit, choose bin with greatest ID

Red Cargo → Largest Fit, choose bin with least ID

Green Cargo → Largest Fit, choose bin with greatest ID

This ensures efficient utilization of space, reduced overhead, and optimal bin usage.

🧠 Problem It Solves

- Traditional cargo systems often lead to fragmentation (unused bin space).
- Choosing bins without strategy causes overflow or failure to fit cargo.
- Lack of adaptability makes it hard to manage different cargo types.

GCMS addresses this by:
- Dynamically assigning cargo to bins based on bin-packing algorithms.
- Allowing flexible policies (Compact Fit / Largest Fit) for different shipment types.
- Supporting efficient search, add, and delete operations with logarithmic complexity.

⚙️ Features
- Add bins with unique IDs and defined capacities.
- Add objects with ID, size, and color (auto-allocated to correct bin).
- Delete objects and free up space in their bin.
- Query object placement and bin details.
- Space and time efficiency using AVL trees for fast lookups.

📂 File Structure
GalacticCargoManagement/

│── gcms.py         # Core cargo management logic

│── bin.py          # Bin representation

│── object.py       # Object representation

│── avl.py          # AVL tree for efficient operations

│── node.py         # AVL node structure

│── exceptions.py   # Custom exceptions (e.g., NoBinFoundException)
│── main.py         # Entry point for testing & running system
│── README.md       # Documentation
