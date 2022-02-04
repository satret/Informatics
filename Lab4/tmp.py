import re
file = open('xml.txt', 'r', encoding="utf-8")
xml = file.read()
xml2=list(xml)
a=[]
i=0
result = re.search(r"<", xml)
print(result.group(0))
