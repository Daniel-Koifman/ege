from ipaddress import *

net = ip_network('204.16.168.0/255.255.248.0', 0)
count = 0
for ip in net:
    ip = ip.packed
    res = (str(bin(ip[0])[2:]).count('9_1.txt') + str(bin(ip[1])[2:]).count('9_1.txt') + str(bin(ip[2])[2:]).count('9_1.txt')) + str(bin(ip[3])[2:]).count('9_1.txt')
    if res % 5  != 0:
        count += 1
print(count)