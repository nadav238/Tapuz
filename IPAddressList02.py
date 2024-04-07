from scapy.all import ARP, Ether, srp
import concurrent.futures
import FindManufacturer
import socket
import FindGatewayIP

def create_IP_range():
    IP = socket.gethostbyname(FindGatewayIP.get_default_gateway_ip())
    IP_List = IP.split(".")
    IP_List.pop(3)
    IP_range = ".".join(IP_List) + ".255/24"
    return IP_range



def get_all_devices_on_network(ip_range):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    result = srp(arp_request, timeout=3, verbose=0)[0]
    devices_list = []
    for sent, received in result:
        devices_list.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices_list

def get_manufacturer_wrapper(device):
    manufacturer = FindManufacturer.get_manufacturer(device['mac'])
    device['manufacturer'] = manufacturer
    return device

if __name__ == "__main__":
    network_ip_range = create_IP_range()
    devices = get_all_devices_on_network(network_ip_range)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        devices_with_manufacturer = list(executor.map(get_manufacturer_wrapper, devices))
    
    print("List of Devices on the Network:")
    for device in devices_with_manufacturer:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
        print(f"Manufacturer: {device.get('manufacturer', 'Unknown')}")