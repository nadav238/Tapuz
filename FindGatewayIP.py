import subprocess

def get_default_gateway_ip():
    try:
        # Get the default gateway using the 'route' command
        result = subprocess.check_output(['route', '-n'])
        result = result.decode('utf-8')

        # Split the output into lines and find the line containing the default gateway
        for line in result.split('\n'):
            if 'UG' in line:
                # Extract the default gateway IP address
                gateway_ip = line.split()[1]
                return gateway_ip

    except Exception as e:
        print(f"Error: {e}")

    return None


if __name__ == "__main__":
    gateway_ip = get_default_gateway_ip()

    if gateway_ip:
        print(f"Default Gateway IP Address: {gateway_ip}")
    else:
        print("Unable to retrieve the default gateway IP address.")
