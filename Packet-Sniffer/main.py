from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())


max_filters=19
opt=0
print("Select a filter:")
print("1-TCP")
print("2-UDP")
print("3-ICMP")
print("4-Certain Port")
print("5-Certain IP")
print("6-All IP packets")
print("7-ARP packets")
print("8-IPv6 Packets")
print("9-HTTP")
print("10-HTTPS")
print("11-DNS")
print("12-SSH")
print("13-NTP")
print("14-HTTP over TCP")
print("15-DNS over TCP")
print("16-DNS over UDP")
print("17-HTTP or HTTPS")
print("18-HTTP to/from specific IP")
print("19-HTTPS to/from specific IP")

while opt<1 or opt>max_filters:
    opt=int(input("Enter option number:"))

filter=""
if opt==1:
    filters="tcp"
elif opt==2:
    filters="udp"        
elif opt==3:
    filters="icmp"    
elif opt==4:
    port=int(input("Enter Port:"))
    filters=f'port {port}' 
elif opt==5:
    IP=str(input("Enter IP:"))
    filter=f'host {IP}'
elif opt==6:
    filter="ip"
elif opt==7:
    filter="arp"               
elif opt==8:
    filter="ip6"
elif opt==9:
    filter="port 80"                   
elif opt==10:
    filter="port 443"   
elif opt==11:
    filter="port 53"                    
elif opt==12:
    filter="tcp port 22"                    
elif opt==13:
    filter="udp port 123"  
elif opt==14:
    filter="tcp and port 80"                      
elif opt==15:
    filter="tcp and port 53"                      
elif opt==16:
    filter="udp and port 53"                      
elif opt==17:
    filter="tcp and (port 80 or port 443)"
elif opt==18:
    IP=str(input("Enter IP:"))
    filter=f'host {IP} and port 80'                      
elif opt==19:
    IP=str(input("Enter IP:"))
    filter=f'host {IP} and port 443'                      


sniff(filter=filter, prn=packet_callback, count=0)    