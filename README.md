# Linux Package Installer

## Overview
Linux Package Installer is a Python-based tool that helps install essential security, networking, and development tools across different Linux distributions. It supports various package managers and provides an easy way to install all or selected packages.

## Features
- Automatic detection of Linux distribution
- Supports multiple package managers (APT, DNF, YUM, Zypper, Pacman)
- Installs a wide range of security, networking, and development tools
- Allows users to install all or selected packages

## Prerequisites
- A Linux-based operating system
- Python 3 installed
- Root or sudo privileges

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/itsmeabhishekrai/Linux-Package-Installer.git
   cd Linux-Package-Installer
   ```
2. Run the script:
   ```bash
   sudo python3 install_packages.py
   ```

## Usage
When you run the script, you will be presented with two options:
1. Install all packages
2. Install selected packages

Example:
```bash
Select an option:
1. Install all packages
2. Install selected packages
Enter your choice (1/2): 2
Available packages:
- nmap
- sqlmap
- wireshark
...
Enter package names separated by space: nmap wireshark
```

## Supported Distributions
- Debian-based (Ubuntu, Kali Linux, etc.)
- Red Hat-based (Fedora, CentOS, etc.)
- Arch-based (Manjaro, EndeavourOS, etc.)
- OpenSUSE

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Author
Abhishek Rai - [GitHub Profile](https://github.com/itsmeabhishekrai)

