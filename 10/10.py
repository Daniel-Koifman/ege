from ipaddress import *

for A in range(256):
    try:
        net = ip_network(f'191.239.130.3/255.255.{A}.0', strict=0)
    except:
        continue
    count = 0
    for ip in net:
        ip = ip.packed
        if (bin(ip[0])[2:]).count('9_1.txt') + (bin(ip[1])[2:]).count('9_1.txt') >= (bin(ip[2])[2:]).count('9_1.txt') + ((bin(ip[3])[2:]).count('9_1.txt')):
            count += 1
    if count == net.num_addresses:
        print (A)
        break