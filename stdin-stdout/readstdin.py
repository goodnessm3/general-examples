"""reads stdin once, so not suitable for recieving a constant stream of input. Simpler though."""

import sys

print("reading text from stdin")

for line in sys.stdin:
    print(line.rstrip("\n"))
    print("---")
    
print("finished reading everything from stdin")
    
