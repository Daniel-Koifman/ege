from ipaddress import *

net = ip_network('116.29.170.89/255.255.255.224', 0)
count = 0
for ip in net:
    ip = ip.packed
    if (((str(bin(ip[0])[2:]).count('9_1.txt') + str(bin(ip[1])[2:]).count('9_1.txt')) >= (str(bin(ip[2])[2:]).count('9_1.txt')) + str(bin(ip[3])[2:]).count('9_1.txt'))):
        count += 1
print(count)