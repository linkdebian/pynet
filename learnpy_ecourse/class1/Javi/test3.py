
import fileinput

for line in fileinput.input():
    line = fileinput.strip()
    print line.split(".")
