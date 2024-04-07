import requests

def get_manufacturer(mac_address):
    api_url = f'https://api.macvendors.com/{mac_address}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve information. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def main():
    # Replace '00:1A:2B:3C:4D:5E' with the MAC address you want to look up
    mac_address = 'a2:b5:3c:f2:24:f0'

    manufacturer_info = get_manufacturer(mac_address)
    print(f"MAC Address: {mac_address}")
    print(f"Manufacturer: {manufacturer_info}")

if __name__ == "__main__":
    main()
