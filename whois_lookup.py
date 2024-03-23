import whois
from colorama import init, Fore, Style
print(" __  __    _    _        _    _  ___   _   ____   ___  _____ _____ ")
print("|  \/  |  / \  | |      / \  | |/ / | | | / ___| / _ \|  ___|_   _|")
print("| |\/| | / _ \ | |     / _ \ | ' /| |_| | \___ \| | | | |_    | |  ")
print("| |  | |/ ___ \| |___ / ___ \| . \|  _  |  ___) | |_| |  _|   | |  ")
print("|_|  |_/_/   \_\_____/_/   \_\_|\_\_| |_| |____/ \___/|_|     |_|  ")

license_text = """
            GNU GENERAL PUBLIC LICENSE
            Version 3, 29 June 2007
            Copyright © 2007 Free Software Foundation, Inc.
            <https://fsf.org/>
            
            This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU General Public License as published by
            the Free Software Foundation, either version 3 of the License, or
            (at your option) any later version.
            
            This program is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
            GNU General Public License for more details.
            
            You should have received a copy of the GNU General Public License
            along with this program.  If not, see <https://www.gnu.org/licenses/>.
            """
print(license_text)
def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        print(Fore.GREEN + "WHOIS Information for:", domain)
        print(Style.RESET_ALL)  # Reset color to default

        if info.domain_name:
            print("Domain Name:", info.domain_name)
        if info.registrar:
            print("Registrar:", info.registrar)
        if info.creation_date:
            print("Creation Date:", info.creation_date)
        if info.expiration_date:
            print("Expiration Date:", info.expiration_date)
        if info.name_servers:
            print("Name Servers:", ', '.join(info.name_servers))
        if info.emails:
            print("Contact Emails:", ', '.join(info.emails))
        if info.address:
            print("Registrant Address:", ', '.join(info.address))

    except Exception as e:
        print(Fore.RED + "Error:", e)
        print(Style.RESET_ALL)  # Reset color to default

def main():
    init(autoreset=True)  # Initialize colorama

    while True:
        domain = input(Fore.LIGHTBLACK_EX + "Enter domain name to perform WHOIS lookup (Q to quit): " + Style.RESET_ALL).strip().lower()

        if domain == 'q':
            print("Exiting the program.")
            break

        print("Performing WHOIS lookup...\n")
        try:
            whois_lookup(domain)
        except Exception as e:
            print(Fore.RED + "Error during WHOIS lookup:", e)
            print(Style.RESET_ALL)

        print("\nWHOIS lookup completed.\n")

if __name__ == "__main__":
    main()
