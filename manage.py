# import os
# import sys
# import tab
# with open("ip.txt","r") as f:
#     print f.readline()
import fileinput
for line in fileinput.input("ip.txt",backup='bak',inplace=0):
    line=line.replace("192.168.0.1","myip")
    print line,