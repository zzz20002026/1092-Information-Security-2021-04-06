import hashlib
import sys

passlist = []
with open('pass.txt', 'r') as f:
    for line in f:
        content = line[:-1]
        passlist.append(content)
if len(sys.argv)>1:
    if sys.argv[1]!='-c':
        msg = sys.argv[1].encode()
        hashvalue = hashlib.sha256(msg)
        print(hashvalue.hexdigest().upper())

    if sys.argv[1]=='-c':
        flag = False
        i=0
        while i<len(passlist[i]) and flag==False:
            if sys.argv[2] == hashlib.sha256(passlist[i].encode()).hexdigest().upper():
                flag = True
                print(passlist[i])
                break
            i = i+1
           
       
