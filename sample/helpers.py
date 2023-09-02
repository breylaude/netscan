import socket
import threading
import psutil
import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Global variables for monitoring and proxy
cpu_threshold = 80.0
memory_threshold = 80.0
proxy_enabled = False
proxy_url = ""
timeout = 1
max_retries = 2
rate_limit = 0.1
auth_username = None
auth_password = None

def monitor_performance():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent

        if cpu_percent > cpu_threshold:
            print(f"CPU Usage Alert: {cpu_percent}%")

        if memory_percent > memory_threshold:
            print(f"Memory Usage Alert: {memory_percent}%")

def scan_port(ip, port):
    for _ in range(max_retries + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)

                if proxy_enabled:
                    sock = requests.get_proxy(sock, proxy_url)

                result = sock.connect_ex((ip, port))

                if result == 0:
                    print(f"Port {port} is open on {ip}")
                    try:
                        banner = sock.recv(1024).decode('utf-8')
                        print(f"Banner: {banner.strip()}")
                    except (socket.timeout, UnicodeDecodeError):
                        pass
                    break
                else:
                    print(f"Port {port} is closed on {ip}")
                    break

        except (socket.error, ConnectionRefusedError):
            pass
        except socket.timeout:
            print(f"Timeout occurred on port {port} of {ip}. Retrying...")
        finally:
            sock.close()

def scan_ip_range(ip_range, port_range):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for ip in ip_range:
            for port in port_range:
                executor.submit(scan_port, ip, port)
                time.sleep(rate_limit)

# Add more core functions or classes as needed

if __name__ == "__main__":
    # You can add a basic command-line interface here to invoke your core functions
    pass
