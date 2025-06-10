import nmap
from colorama import init, Fore, Style
import json
import time
import sys
import threading

init()


def loading_animation(stop_event):
    symbols = ['|', '/', '-', '\\']
    i = 0
    while not stop_event.is_set():
        print(f"\rScanning... {symbols[i % len(symbols)]}", end="")
        time.sleep(0.1)
        i += 1
    print("\rScan complete!          ")


def print_ports(title, ports_dict):
    color = {
        "Open Ports": Fore.GREEN,
        "Closed Ports": Fore.RED,
        "Filtered Ports": Fore.YELLOW,
        "Unfiltered Ports": Fore.BLUE,
        "Open|Filtered Ports": Fore.MAGENTA,
        "Closed|Filtered Ports": Fore.CYAN
    }.get(title, Fore.WHITE)

    print(f"{color}{title}:{Style.RESET_ALL}")
    if not ports_dict:
        print(" (none)")
    else:
        for port, service in ports_dict.items():
            print(f"{color}Port {port}: {service[0]} , Protocol: {service[1]}{Style.RESET_ALL}")
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

def main():
    ip_domain=input("Enter IP or Domain:")
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
    full_range = input("Scan full port range? (Yes/No): ")
    if full_range.lower() == 'yes':
        print(Fore.YELLOW + "[!] Full port range scan selected. This may take several minutes..." + Style.RESET_ALL)
        ports = "1-65535"
    else:
        ports = ",".join(str(port) for port in common_ports.keys())

    # Start loading animation in a thread
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loading_thread.start()

    scanner=nmap.PortScanner()

    start_time=time.time()

    # Do the actual scan
    try:
        try:
            if(option==3):
                state = scanner.scan(hosts=ip_domain, arguments=f"-sS -sU -sV -p T:{ports},U:{ports} ")
            elif(option==2):
                state = scanner.scan(hosts=ip_domain, arguments=f"-sU -sV -p U:{ports}")
            else:
                state = scanner.scan(hosts=ip_domain, arguments=f"-sS -sV -p T:{ports}")
        except nmap.PortScannerError as e:
            print(Fore.RED + f"Error: Scan failed – {e}" + Style.RESET_ALL)
            retry = input("Scan failed. Try again? (Yes/No): ")
            if retry.lower() == 'yes':
                main()
            sys.exit(1)
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}" + Style.RESET_ALL)
            sys.exit(1)
    finally:
        stop_event.set()
        loading_thread.join()


    end_time=time.time()
    duration=end_time-start_time

    if ip_domain not in scanner.all_hosts():
        print(Fore.RED + f"Error: Host '{ip_domain}' is unreachable or unknown." + Style.RESET_ALL)
        sys.exit(1)


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
    print(f"\nScan completed in {int(duration)} seconds.\n")
    print_ports("Open Ports", open_ports)
    print_ports("Closed Ports", closed_ports)
    print_ports("Filtered Ports", filtered_ports)
    print_ports("Unfiltered Ports", unfiltered_ports)
    print_ports("Open|Filtered Ports", open_filtered_ports)
    print_ports("Closed|Filtered Ports", closed_filtered_ports)

    flag=False
    for port in open_ports:
        if port in common_ports and common_ports[port][1]==1:
            print(Fore.RED + f"WARNING! Sensitive Port {port}: {common_ports[port][0]} is open via {open_ports[port][1]}" + Style.RESET_ALL)
            flag=True
    if not flag:
        print("Congratulations! No sensitive ports open")        

    print("Summary:")
    print("Open Ports: ",len(open_ports))
    print("Closed Ports: ",len(closed_ports))
    print("Filtered Ports: ",len(filtered_ports))
    print("Unfiltered Ports: ",len(unfiltered_ports))
    print("Open Filtered Ports: ",len(open_filtered_ports))
    print("Closed Filtered Ports: ",len(closed_filtered_ports))

    file_option=input("Do you want to save results to a file?(Yes/No):")
    if (file_option.lower()=="yes"):
        format_option=input("Enter File Format(txt/json):")
        file_name=input("Enter File Name(Without Extension):")
        if format_option.lower()=="txt":
            write_results_to_txt(file_name,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports)
        elif format_option.lower()=="json":
            write_results_to_json(file_name,open_ports,closed_ports, filtered_ports, unfiltered_ports, open_filtered_ports,closed_filtered_ports)

if __name__ == '__main__':
    main()