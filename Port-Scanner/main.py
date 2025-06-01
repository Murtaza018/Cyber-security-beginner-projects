import nmap
from colorama import init, Fore, Style
import json


init()

def print_ports(title, ports_dict):
    print(f"{title}:")
    if not ports_dict:
        print(" (none)")
    else:
        for port, service in ports_dict.items():
            print(f"Port {port}: {service[0]} , Protocol: {service[1]}")
    print()

def write_results_to_txt(filename,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports):
    with open(filename + ".txt", "w") as file:

        def write_section(title, ports_dict):
            file.write(f"{title}:\n")
            if ports_dict:
                for port, service in ports_dict.items():
                    file.write(f"Port {port}: {service[0]} , Protocol: {service[1]}\n")
            else:
                file.write("None\n")
            file.write("\n")

        write_section("Open Ports", open_ports)
        write_section("Closed Ports", closed_ports)
        write_section("Filtered Ports", filtered_ports)
        write_section("Unfiltered Ports", unfiltered_ports)
        write_section("Open|Filtered Ports", open_filtered_ports)
        write_section("Closed|Filtered Ports", closed_filtered_ports)


def write_results_to_json(filename,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports):
    def format_ports_dict(port_dict):
        if port_dict:
            return {str(port): {'service': val[0], 'protocol': val[1]} for port, val in port_dict.items()}
        else:
            return None

    json_data = {
        "Open Ports": format_ports_dict(open_ports),
        "Closed Ports": format_ports_dict(closed_ports),
        "Filtered Ports": format_ports_dict(filtered_ports),
        "Unfiltered Ports": format_ports_dict(unfiltered_ports),
        "Open|Filtered Ports": format_ports_dict(open_filtered_ports),
        "Closed|Filtered Ports": format_ports_dict(closed_filtered_ports),
    }

    with open(filename + ".json", "w") as file:
        json.dump(json_data, file, indent=4)


ip_domain=input("Enter IP or Domain:")
print(ip_domain)
print("Choose Scan Type (Wrong option number will automatically choose default)")
print("1-TCP (Default)")
print("2-UDP")
print("3-Both TCP and UDP")
option=input("Enter option number:")
option = option.strip()
if option not in [1,2,3]:
    option = 1


common_ports={
21 :["FTP",1],
22 :["SSH",1],
23 : ["Telnet",1],
25 : ["SMTP",0],
53 : ["DNS",0],
80 : ["HTTP",0],
443 : ["HTTPS",0],
445:["SMB",1],
3306 : ["MySQL",0],
3389 : ["RDP",1],
}
print(common_ports)

scanner=nmap.PortScanner()
ports = ",".join(str(port) for port in common_ports.keys())
if(option==3):
    state = scanner.scan(hosts=ip_domain, arguments=f"-sS -sU -p T:{ports},U:{ports}")
elif(option==2):
    state = scanner.scan(hosts=ip_domain, arguments=f"-sU -p U:{ports}")
else:
    state = scanner.scan(hosts=ip_domain, arguments=f"-sS -p T:{ports}")
open_ports={}
closed_ports={}
filtered_ports={}
unfiltered_ports={}
open_filtered_ports={}
closed_filtered_ports={}
if option !=2:
    for port in scanner[ip_domain]['tcp']:
        if scanner[ip_domain]['tcp'][port]['state'] == 'open':
            open_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']  
        elif scanner[ip_domain]['tcp'][port]['state'] == 'closed':    
            closed_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
        elif scanner[ip_domain]['tcp'][port]['state'] == 'filtered':
            filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
        elif scanner[ip_domain]['tcp'][port]['state'] == 'unfiltered':
            unfiltered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
        elif scanner[ip_domain]['tcp'][port]['state'] == 'open|filtered':
            open_filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
        elif scanner[ip_domain]['tcp'][port]['state'] == 'closed|filtered':
            closed_filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']

if option ==2 or option==3:
    for port in scanner[ip_domain]['udp']:
        if scanner[ip_domain]['udp'][port]['state'] == 'open':
            open_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']  
        elif scanner[ip_domain]['udp'][port]['state'] == 'closed':    
            closed_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
        elif scanner[ip_domain]['udp'][port]['state'] == 'filtered':
            filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
        elif scanner[ip_domain]['udp'][port]['state'] == 'unfiltered':
            unfiltered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
        elif scanner[ip_domain]['udp'][port]['state'] == 'open|filtered':
            open_filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
        elif scanner[ip_domain]['udp'][port]['state'] == 'closed|filtered':
            closed_filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
     
print(f"Scan type selected: {'TCP only' if option == '1' else 'UDP only' if option == '2' else 'Both TCP and UDP'}")
print_ports("Open Ports", open_ports)
print_ports("Closed Ports", closed_ports)
print_ports("Filtered Ports", filtered_ports)
print_ports("Unfiltered Ports", unfiltered_ports)
print_ports("Open|Filtered Ports", open_filtered_ports)
print_ports("Closed|Filtered Ports", closed_filtered_ports)

flag=False
for port in open_ports:
    if common_ports[port][1]==1:
        print(Fore.RED + f"WARNING! Sensitive Port {port}: {common_ports[port][0]} is open via {open_ports[port][1]}" + Style.RESET_ALL)
        flag=True
if not flag:
    print("Congratulations! No sensitive ports open")        

file_option=input("Do you want to save results to a file?(Yes/No):")
if (file_option.lower()=="yes"):
    format_option=input("Enter File Format(txt/json):")
    file_name=input("Enter File Name(Without Extension):")
    if format_option.lower()=="txt":
        write_results_to_txt(file_name,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports)
    elif format_option.lower()=="json":
        write_results_to_json(file_name,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports)