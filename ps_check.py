import dns.resolver
from tabulate import tabulate
import os
import sys

def print_banner():
    banner = r"""
         _          _                  _             _       _    _             _             _        
'########:::'######::::::'######::'##::::'##:'########::'######::'##:::'##:
 ##.... ##:'##... ##::::'##... ##: ##:::: ##: ##.....::'##... ##: ##::'##::
 ##:::: ##: ##:::..::::: ##:::..:: ##:::: ##: ##::::::: ##:::..:: ##:'##:::
 ########::. ######::::: ##::::::: #########: ######::: ##::::::: #####::::
 ##.....::::..... ##:::: ##::::::: ##.... ##: ##...:::: ##::::::: ##. ##:::
 ##::::::::'##::: ##:::: ##::: ##: ##:::: ##: ##::::::: ##::: ##: ##:. ##::
 ##::::::::. ######:::::. ######:: ##:::: ##: ########:. ######:: ##::. ##:
..::::::::::......:::::::......:::..:::::..::........:::......:::..::::..::                                                                         
    
                🔍 PS CHECK - A Python script to check if domains are blacklisted 🔍
    """
    print(banner)

def install_requirements():
    print("Checking and installing required packages...")
    try:
        import pip
        os.system(f"{sys.executable} -m pip install dnspython tabulate")
    except Exception as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

def get_user_domains():
    print("\nEnter domain names to check. You can enter a single domain or a list separated by commas.")
    user_input = input("Enter domain(s): ").strip()
    if "," in user_input:
        return [domain.strip() for domain in user_input.split(",") if domain.strip()]
    else:
        return [user_input] if user_input else []

# List of popular DNS Blacklist providers (RBLs)
rbls = [
    "zen.spamhaus.org", "bl.spamcop.net", "b.barracudacentral.org",
    "dnsbl.sorbs.net", "spam.dnsbl.sorbs.net", "bl.spamcop.net"
]

def check_blacklist(domain):
    """Check if the domain is blacklisted on any RBL provider."""
    try:
        for rbl in rbls:
            query = f"{domain}.{rbl}"
            try:
                dns.resolver.resolve(query, "A")
                return [domain, "YES"]  # Blacklisted
            except dns.resolver.NXDOMAIN:
                continue  # Not listed on this RBL
        return [domain, "NO"]  # Not blacklisted
    except Exception:
        return [domain, "ERROR"]  # Error checking domain

if __name__ == "__main__":
    print_banner()
    install_requirements()
    domains = get_user_domains()
    if not domains:
        print("No domains entered. Exiting.")
        sys.exit(0)
    
    print("\nChecking blacklist status...")
    table_data = [check_blacklist(domain) for domain in domains]
    headers = ["Domain", "Blacklisted"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
