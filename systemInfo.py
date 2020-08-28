#A little module to get system information 
#in development
import platform,socket
from socket import *
def system():
    print("systemInfo 0.4")
    print("Host Name: " + platform.node())
    print("OS: " + platform.system() + " " + platform.release() + " " + platform.win32_edition())
    print("IP: " + socket.gethostbyname(socket.gethostname()))

def port_scanner():
    target = input("Enter IP: ")
    target = gethostbyname(target)
    print("Starting scan...")
    for i in range(1, 500):
        if(socket(AF_INET, SOCK_STREAM).connect_ex((target, i)) == 0) :
            print("Port %d: open" % (i,))
        socket(AF_INET, SOCK_STREAM).close()
    print("Done")
    
system()
port_scanner()

'''
def ip_ddos():
    target = input("Enter IP:")
    tPort = input("Enter Port:")
    sIP = socket.gethostbyname(socket.gethostname())
    i = 1
    for x in range(0, 1000):
        ip = IP(source_IP = sIP, destination = target)
        TCP1 = TCP(srcport = 80, dstport = tPort)
        pkt = IP1 / TCP1
        send(pkt, inter = .001)
   
        print ("Packet sent ", i)
        i + 1 
'''
