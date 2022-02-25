# CPE315-Quarter-Project

### Tyler Bovenzi - Shae Li - John Kroska

## Usage:

Arm Side

1. Compile main.c without compiler optimization
   1. gcc main.c -O0 -o main -std=c99 -lm
   2. This is the executable used to record cache misses within the python function
2. Execute main.py
   1. This cycles through possible data chunk sizes and records cache performance
   2. Output CSV data is saved as L1.txt and L2.txt (space delimited)

Windows/Mac/UserOS side

1. Ensure python is installed
2. pip install matplotlib
3. Ensure L1.txt and L2.txt are in the same directory as graph.py
4. python graph.py
   1. This should create a window with a graph of cache misses vs chunk size

## TODO:

* Test on a different arm device with known cache values (Raspberry Pi)
* Equate cache data to from graph to physical and detemine actual L1 and L2 size
* Potentially streamline execution process such that the python code automatically executes C code
* L3? - Might be difficult since arm perf does not report L3 cache data
* Document Document Document
