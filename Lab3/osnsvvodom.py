import re
n=int(input())
for testnumber in range(n):
    str = tests[testnumber]
    s = re.findall(r":-\(", str)
    k=len(s)
    print(k)
#:-(
