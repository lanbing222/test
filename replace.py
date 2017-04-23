import fileinput
for line in fileinput.input("ip.txt",backup='bak',inplace=1):
    line=line.replace("myip","192.168.0.1")
    print line,