"""reads anything from stdin and prints it."""

import sys
import time

print("running")


line = sys.stdin.readline()
while line:
    print(line)
    print("---")
    line = sys.stdin.readline()
 
print("exited")
    
