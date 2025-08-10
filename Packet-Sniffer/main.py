from scapy.all import sniff
from scapy.all import wrpcap
from scapy.all import get_if_list
from datetime import datetime

global_count = 0
def packet_callback(packet):
    if verbose:
        packet.show()
    else:
        global global_count
        global_count += 1
        print(f"#{global_count} [{datetime.now().strftime('%H:%M:%S')}] {packet.summary()}")
        

interfaces = get_if_list()
print("\nAvailable interfaces:")
for i, iface in enumerate(interfaces):
    print(f"{i + 1} - {iface}")

iface_index = int(input("Select interface number: ")) - 1
iface_name = interfaces[iface_index]

max_filters=19
opt=0
print("Select a filter:")
print("1 - TCP")
print("2 - UDP")
print("3 - ICMP")
print("4 - Certain Port")
print("5 - Certain IP")
print("6 - All IP packets")
print("7 - ARP packets")
print("8 - IPv6 Packets")
print("9 - HTTP")
print("10 - HTTPS")
print("11 - DNS")
print("12 - SSH")
print("13 - NTP")
print("14 - HTTP over TCP")
print("15 - DNS over TCP")
print("16 - DNS over UDP")
print("17 - HTTP or HTTPS")
print("18 - HTTP to/from specific IP")
print("19 - HTTPS to/from specific IP")
print("20 - TCP from specific IP")
print("21 - UDP to specific IP")



while opt<1 or opt>max_filters:
    opt=int(input("Enter option number:"))

filters=""
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
    filters=f'host {IP}'
elif opt==6:
    filters="ip"
elif opt==7:
    filters="arp"               
elif opt==8:
    filters="ip6"
elif opt==9:
    filters="port 80"                   
elif opt==10:
    filters="port 443"   
elif opt==11:
    filters="port 53"                    
elif opt==12:
    filters="tcp port 22"                    
elif opt==13:
    filters="udp port 123"  
elif opt==14:
    filters="tcp and port 80"                      
elif opt==15:
    filters="tcp and port 53"                      
elif opt==16:
    filters="udp and port 53"                      
elif opt==17:
    filters="tcp and (port 80 or port 443)"
elif opt==18:
    IP=str(input("Enter IP:"))
    filters=f'host {IP} and port 80'                      
elif opt==19:
    IP=str(input("Enter IP:"))
    filters=f'host {IP} and port 443'                      
elif opt == 20:
    IP = input("Enter source IP: ")
    filters = f"src host {IP} and tcp"
elif opt == 21:
    IP = input("Enter destination IP: ")
    filters = f"dst host {IP} and udp"


verbose = input("Show full packet details? (y/n): ").lower() == 'y'
count = int(input("Enter number of packets to capture (0 for unlimited): "))
try:
    packets=sniff(filter=filters, iface=iface_name,prn=packet_callback, count=0 if count == 0 else count)
    wrpcap("captured_packets.pcap", packets)
    print("\nPackets saved to captured_packets.pcap")
except KeyboardInterrupt:
    print("\nSniffing stopped by user.") 