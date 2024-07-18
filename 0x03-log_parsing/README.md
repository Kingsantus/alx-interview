# Log Parsing

## Description
This repository contains two Python scripts: 0-stats.py and 0-generator.py.

### 0-stats.py: Reads lines from standard input, parses them as log entries, and computes metrics such as the total file size and the count of each status code. It prints these metrics after every 10 lines and upon termination.
### 0-generator.py: Generates simulated log entries and outputs them to standard output, which can be piped into 0-stats.py for testing purposes.

### ./0-generator.py | ./0-stats.py 
