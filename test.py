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
        hashvalue2 = hashlib.sha512(msg)
        hashvalue3 = hashlib.sha1(msg)
        hashvalue4 = hashlib.md5(msg)
        print("sha-256: ", hashvalue.hexdigest().upper())
        print("sha-512: ", hashvalue2.hexdigest().upper())
        print("sha-1: ", hashvalue3.hexdigest().upper())
        print("MD5: ", hashvalue4.hexdigest().upper())

    if sys.argv[1]=='-c':
        flag = False
        i=0
        while i<len(passlist[i]) and flag==False:
            if sys.argv[2] == hashlib.sha256(passlist[i].encode()).hexdigest().upper():
                flag = True
                print(passlist[i])
                break
            elif sys.argv[2] == hashlib.sha512(passlist[i].encode()).hexdigest().upper():
                flag = True
                print(passlist[i])
                break
            elif sys.argv[2] == hashlib.sha1(passlist[i].encode()).hexdigest().upper():
                flag = True
                print(passlist[i])
                break
            elif sys.argv[2] == hashlib.md5(passlist[i].encode()).hexdigest().upper():
                flag = True
                print(passlist[i])
                break
            i = i+1
           
       
