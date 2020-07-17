"""Generates a bunch of data, then feeds it into another script using subprocess.
Waits for the subprocess to finisn."""

import subprocess

print("generating stream for stdin")
content = ""
for x in range(10):
	content += f"Line {x}\n"
	
q = subprocess.run("python readstdin.py", input=content, text=True)
print("content generator finished")
print(q.returncode)

