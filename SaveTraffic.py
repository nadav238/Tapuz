import scapy

# Define the target IP address
target_ip = "192.168.1.10"  # Replace with the specific IP address

# Filter expression to capture traffic to or from the target IP
filter_expression = f"ip src {target_ip} or ip dst {target_ip}"

def capture_packets(packet):
    # Check if the packet is related to the target IP (source or destination)
    if (packet.haslayer(scapy.IP()) and (packet[scapy.IP()].src == target_ip or packet[scapy.IP()].dst == target_ip)):
        print(packet.summary())  # Print packet summary (optional)
        scapy.wrpcap("captured_packets.pcapng", packet)  # Save the packet

# Start capturing packets with the filter applied
scapy.sniff(count=0, filter=filter_expression, prn=capture_packets)  # Capture indefinitely (count=0)
