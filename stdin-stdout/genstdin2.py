"""constantly generates a stream of lines to be fed into the reader program"""

import subprocess
import time

print("generating stream for stdin")
	
q = subprocess.Popen("python readstdin2.py", stdin=subprocess.PIPE)
x = 0

while 1:
    print("in loop")
    x += 1
    if x == 10:
        break
    else:
        outstr = f"Line {x}\n".encode("UTF-8")

    q.stdin.write(outstr)
    q.stdin.flush()  # force the output to the receiving program, otherwise it will stay in the buffer
    # that is fine but we want to watch the programs running simultaneously
    time.sleep(0.1)

    
        

