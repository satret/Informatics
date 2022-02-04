import re
tests = ["ri:-)pgujk:-(fuu:-(urifreoisd:-(kjfepi;uer:(",
         ";oiuytgf:-(gbnm,.;'[pvfde56:-(7890-098765434",
         "oiuyt:-(redsdxcvbhji:-(oiuyhgvb:-(hjklop;lkj",
         "bkjkninl;lmojiph:-(pijknliug67568y0u9-i0:-(",
         "uugiy8599870-09=09087546687986079*%#:-(",
         "pei4holkwlesdvoetkn;lwreh4865783470359-02i3["]
for testnumber in range(len(tests)):
    str = tests[testnumber]
    s = re.findall(r":-\(", str)
    k=len(s)
    print(k)
#:-(
