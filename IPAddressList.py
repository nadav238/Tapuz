from scapy.all import ARP, Ether, srp
import FindManufacturer
import socket
import FindGatewayIP

def create_IP_range():
    IP = socket.gethostbyname(FindGatewayIP.get_default_gateway_ip())
    IP_List = IP.split(".")
    IP_List.pop(3)
    IP_range = ".".join(IP_List) + ".255/24"
    return IP_range

def get_all_devices_on_network():
    ip_range = create_IP_range()
    # Create an ARP request packet to get the MAC addresses of devices in the specified IP range
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)

    # Send the ARP request and capture the response
    result = srp(arp_request, timeout=3, verbose=0)[0]

    # Extract the IP and MAC addresses from the response
    devices_list = []
    for sent, received in result:
        devices_list.append({'ip': received.psrc, 'mac': received.hwsrc, 'manufacturer' : FindManufacturer.get_manufacturer(received.psrc)})

    return devices_list

if __name__ == "__main__":
    # Specify the IP range for the network (e.g., "192.168.1.1/24")
    #network_ip_range = "10.68.213.255/24"

    # Get the list of devices on the network
    devices = get_all_devices_on_network()

    # Print the list of devices
    print("List of Devices on the Network:")
    for device in devices:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
        #print(f"Manufcturer: {FindManufacturer.get_manufacturer(device['mac'])}")