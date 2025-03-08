import os
import subprocess
import platform
import shutil

def detect_linux_version():
    try:
        with open("/etc/os-release") as f:
            info = {}
            for line in f:
                key, value = line.strip().split("=", 1)
                info[key] = value.strip('"')
            return info.get("ID"), info.get("VERSION_ID")
    except Exception as e:
        print(f"Error detecting Linux version: {e}")
        return None, None

def check_sudo():
    if os.name == "nt":
        print("This script is only for Linux systems.")
        return False
    try:
        if os.geteuid() != 0:
            print("Please run this script as root or with sudo.")
            return False
    except AttributeError:
        if os.environ.get("SUDO_UID") is None:
            print("Please run this script as root or with sudo.")
            return False
    return True

def install_packages(packages):
    if not check_sudo():
        return
    
    system = platform.system()
    if system != "Linux":
        print("This script is only for Linux systems.")
        return
    
    distro, version = detect_linux_version()
    print(f"Detected Linux distribution: {distro} {version}")
    
    package_managers = {
        "APT": ["apt", "install", "-y"],
        "DNF": ["dnf", "install", "-y"],
        "YUM": ["yum", "install", "-y"],
        "Zypper": ["zypper", "install", "-y"],
        "Pacman": ["pacman", "-S", "--noconfirm"]
    }
    
    manager = None
    for pm in package_managers.keys():
        if shutil.which(package_managers[pm][0]):
            manager = pm
            break
    
    if not manager:
        print("Unsupported package manager. Install packages manually.")
        return
    
    print(f"Using {manager} to install packages...")
    try:
        if manager == "APT":
            subprocess.run([shutil.which("apt"), "update"], check=True)
        
        for package in packages:
            if package in ["mysql-server", "netcat", "docker"]:
                print(f"Skipping unavailable package: {package}")
                continue
            try:
                subprocess.run([shutil.which(package_managers[manager][0])] + package_managers[manager][1:] + [package], check=True)
            except subprocess.CalledProcessError:
                print(f"Error: Unable to install package {package}. Skipping...")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")

def main():
    packages_to_install = [
        "nmap", "metasploit-framework", "sqlmap", "wireshark", "aircrack-ng", "john", "burpsuite", "hydra",
        "lynis", "autopsy", "maltego", "nikto", "wpscan", "hashcat", "skipfish", "apktool",
        "bettercap", "beef", "yersinia", "arp-scan", "traceroute", "build-essential", "gcc", "g++", "make",
        "python3", "python3-pip", "perl", "ruby", "git", "curl", "wget", "openssl", "libssl-dev", "zlib1g-dev",
        "libffi-dev", "libpcap-dev", "dnsutils", "whois", "iptables", "tcpdump", "binwalk", "foremost", "radare2",
        "gdb", "strace", "ltrace", "htop", "iftop", "iotop", "screen", "tmux", "vim", "nano", "tree", "rsync",
        "httrack", "proxychains", "tor", "ufw", "fail2ban", "net-tools", "cowsay", "lolcat", "cmatrix", "sqlninja",
        "fcrackzip", "medusa", "masscan", "snort", "suricata", "zaproxy", "recon-ng", "theharvester", "spiderfoot",
        "subfinder", "amass", "enum4linux", "nbtscan", "cewl", "crunch", "hash-identifier", "hping3", "dmitry",
        "ettercap-graphical", "reaver", "nodejs", "npm", "default-jdk", "default-jre", "golang", "rustc", "cargo",
        "php", "php-cli", "php-curl", "php-xml", "php-mbstring", "php-zip", "php-json", "php-soap", "php-bcmath",
        "php-intl", "php-gd", "php-sqlite3", "php-pgsql", "lua5.3", "r-base", "r-cran-tidyverse", "octave",
        "openjdk-11-jdk", "cmake", "clang", "lldb", "lld", "texlive-full", "apache2", "nginx", "postgresql",
        "redis", "docker-compose"
    ]
    
    print("\nSelect an option:")
    print("1. Install all packages")
    print("2. Install selected packages")
    
    try:
        choice = input("Enter your choice (1/2): ").strip()
        if choice == "1":
            install_packages(packages_to_install)
        elif choice == "2":
            print("Available packages:")
            for package in packages_to_install:
                print(f"- {package}")
            selected_packages = input("Enter package names separated by space: ").split()
            install_packages(selected_packages)
        else:
            print("Invalid choice. Exiting.")
    except (EOFError, ValueError):
        print("Error: Unable to read user input. Run the script in an interactive terminal.")

if __name__ == "__main__":
    main()

