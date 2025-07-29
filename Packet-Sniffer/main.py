from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())


sniff(prn=packet_callback, count=0)
sniff(filter="tcp port 80", prn=packet_callback, count=0)


print("Select a filter:")
print("1-TCP")
print("2-UDP")
print("3-ICMP")
print("4-Certain Port")
print("5-Certain IP")
print("6-All IP packets")
print("7-ARP packets")
print("8-IPv6 Packets")