# with open("ip.txt",'r+') as f:
#     for line in f.readlines():
#         if '192.168.0.11' in line:
#             print line
#             print f.tell()
# f.close()
from _ast import Num

f=file("ip.txt",'r+')

# for line in f.readlines()   :
#     if '192.168.0.11' in line:
#         print line
#         num = line.find("192.168.0.11")
#         
# 
# #     
n=0
while True:
    line=f.readline()
    if line=="":
        break
    else:
        if "192.168.0.20" in line:
            print line,
            print n
            num=line.find("192.168.0.20")
            num_list=n+num
            print num_list
            f.seek(num_list)
            f.write("192.168.1.20")
            break
        else:
            n=f.tell()
            continue
            