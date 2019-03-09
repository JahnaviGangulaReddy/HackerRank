# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python
import sys
def coor(co):
	 final = []
	 l1 = [i for i in range(0,co[0]+1)]
	 l2 = [i for i in range(0,co[1]+1)]
	 l3 = [i for i in range(0,co[2]+1)]
	 limit = co[3]
	 z = [[a,b,c] for a in l1 for b in l2 for c in l3 if a+b+c != limit]
	 print z

if __name__ == "__main__":
	val = []
	for i in range(0,4):
		b = int(sys.stdin.readline())
		val.append(b)
	coor(val)
