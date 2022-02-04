import time
start_time = time.time()
file = open('xml.txt', 'r', encoding="utf-8")
json = open('json.txt', 'w')
xml = file.read()
xml2=[]
k=len(xml)-1
for i in range(k):
    j=i+1
    w=j+1
    if xml[i]=='<' and xml[j]=='/' and xml[w]=='l':
        xml = xml.replace('</lesson', '}       ', 1)
        print('}', end ="", file=json)
        
    if xml[i]=='<' and xml[j]=='/' and xml[w]=='d':
        xml = xml.replace('</day', '}    ', 1)
        
        
    if xml[i]=='<' and xml[j]=='/' and xml[w]=='s':
        xml = xml.replace('</schedule', '}         ', 1)
        
    if xml[i]=='e' and xml[j]=='>':
        xml = xml.replace('>   ', '\": {', 1)
        
    if xml[i]=='<':
        xml = xml.replace('<', '\"', 1)
        
    if xml[i]=='>':
        xml = xml.replace('>', ' ', 1)

    if xml[i]=='=':
        xml = xml.replace('=', ' ', 1)
        print('\":', end ="", file=json)
        
    if xml[i]==' ' and xml[j]=='n':
        print('\":{', file=json)
        xml = xml.replace(' n', '\"n', 1)
        
    if xml[i]==' ' and xml[j]=='t':
        print('\":{', file=json)
        xml = xml.replace(' t', '\"t', 1)
        
    if xml[i]==' ' and xml[j]=='a':
        print('\":{', file=json)
        xml = xml.replace(' a', '\"a', 1)
        
    if xml[i]==' ' and xml[j]=='f':
        print('\":{', file=json)
        xml = xml.replace(' f', '\"f', 1)

    if xml[i]==' ' and xml[j]=='b':
        print('\":{', file=json)
        xml = xml.replace(' b', '\"b', 1)
        
    if xml[i]=='/':
        xml = xml.replace('/', '}', 1)
    print(xml[i], end ="", file=json)

json.close()
print("--- %s seconds ---" % (time.time() - start_time))
