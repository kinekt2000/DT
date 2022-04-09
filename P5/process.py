from math import sqrt
import matplotlib.pyplot as plt

file = open("output.txt", "r")

xyz = []

equ = []

for line in file:
    s = line.strip()
    if (s.startswith("(x,y,z)")):
        numbers = s.split("=")[1].strip()[1:-1].split(",")
        numbers = tuple(map(lambda s: float(s.strip()), numbers))
        xyz.append(numbers)

    if (s.startswith("RA")):
        ra = equ[5:17]
        print(ra)
        equ.append(s)

equ.pop(0)
xyz.pop(0)

for e in equ:
    print(e)

def diff(a, b):
    return (
        a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2],
    )

def dist(v):
    return sqrt(v[0]**2 + v[1]**2 + v[2]**2)


diffs = []

for i in range(30):
    before = xyz[i*2]
    after = xyz[i*2+1]

    diffs.append(dist(diff(before, after)))

plt.plot(diffs)
plt.grid(True, "both")
# plt.axhline(min(diffs))
# plt.axhline(max(diffs))
plt.show()

print(min(diffs))
print(max(diffs))