f = open ("myContact.txt")
print(f) #CP1252 encoding
f = open("myContact.txt",'w') # write in text mode
#f = open("README.md",'r+b') # read and write in binary mode

f = open("myContact.txt", mode = 'w', encoding = 'utf-8')
print(f) #UTF-8 encoding
f.close()


try:
    f=open("myContact.txt",encoding = 'utf-8')
    print(f.readlines())
except:
    print("Error")
finally:
    f.close()
'''
'''
with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

with open("test.txt",'r',encoding = 'utf-8') as f:
    print(f.read())

import fnmatch
import os

for filename in os.listdir('.'): # Run a for loop
    if fnmatch.fnmatch(filename,'*.txt'): #test whether given filename string matches the pattern strings
        print(filename)
