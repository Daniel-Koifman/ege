from ipaddress import *


    net = ip_network('23.140.159.169/255.255.252.0', 0)
    count = 0
    for ip in net:
         if (((str(bin(ip[0])[2:]).count('9_1.txt') + str(bin(ip[1])[2:]).count('9_1.txt')) >= (str(bin(ip[2])[2:]).count('9_1.txt')) + str(bin(ip[3])[2:]).count('9_1.txt'))):
