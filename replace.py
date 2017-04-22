import fileinput
for line in fileinput.input("ip.txt",backup='bak',inplace=0):
    line=line.replace("192.168.0.1","myip")
    print line,