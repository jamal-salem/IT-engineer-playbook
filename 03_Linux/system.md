# Linux System Fundamentals

This section explains how Linux works internally.

Topics include:
- Kernel and user space
- Processes and signals
- Filesystem hierarchy
- Permissions and ownership

The goal is to understand system behavior, not memorize commands.



```bash

# Linux Essential Commands

# File & Directory

pwd                         # Show current directory
ls                          # List files
ls -l                       # Detailed list
ls -la                      # Show hidden files
cd folder                   # Enter folder
cd ..                       # Go back one directory
cd ~                        # Go to home directory
mkdir folder                # Create folder
mkdir folder1 folder2       # Create multiple folders
rmdir folder                # Remove empty folder
rm file.txt                 # Delete file
rm -r folder                # Delete folder
rm -rf folder               # Force delete folder
touch file.txt              # Create empty file
cp file.txt backup.txt      # Copy file
cp -r folder backup         # Copy folder
mv old.txt new.txt          # Rename file
mv file.txt Documents/      # Move file

# View Files

cat file.txt                # Display file
less file.txt               # View file page by page
head file.txt               # First 10 lines
tail file.txt               # Last 10 lines
tail -f logfile.log         # Follow log file live

# Search

find . -name "*.txt"        # Find files
grep "text" file.txt        # Search inside file
grep -r "text" .            # Search recursively

# Permissions

ls -l                       # View permissions
chmod +x script.sh          # Make executable
chmod 755 script.sh         # Change permissions
chown user:user file.txt    # Change owner

# Users

whoami                      # Current user
id                          # User information
passwd                      # Change password
sudo command                # Run as administrator

# Disk & Storage

lsblk                       # List disks
df -h                       # Disk usage
du -sh folder               # Folder size

# Memory

free -h                     # RAM usage

# System Information

hostname                    # Computer name
hostname -I                 # IP Address
uname -a                    # Kernel information
cat /etc/os-release         # OS version
lscpu                       # CPU information
cat /proc/meminfo           # Memory details
neofetch                    # System summary

# Networking

ip a                        # Network interfaces
ip route                    # Routing table
ping google.com             # Test connectivity
ss -tuln                    # Open ports
netstat -tulnp              # Network connections (if installed)

# Process Management

ps aux                      # Running processes
top                         # Live process monitor
htop                        # Better process monitor
kill PID                    # Kill process
kill -9 PID                 # Force kill process

# Package Management (APT)

sudo apt update             # Update repositories
sudo apt upgrade            # Upgrade packages
sudo apt full-upgrade       # Full system upgrade
sudo apt install package    # Install package
sudo apt remove package     # Remove package
sudo apt purge package      # Remove package completely
sudo apt autoremove         # Remove unused packages
apt search package          # Search package

# Services

systemctl status service    # Service status
sudo systemctl start service
sudo systemctl stop service
sudo systemctl restart service
sudo systemctl enable service
sudo systemctl disable service

# Archives

zip -r archive.zip folder
unzip archive.zip
tar -czvf archive.tar.gz folder
tar -xzvf archive.tar.gz

# Download Files

wget URL
curl -O URL

# Shutdown

sudo reboot
sudo shutdown now
sudo poweroff

# Useful Shortcuts

Ctrl + C        # Stop current command
Ctrl + Z        # Suspend process
Ctrl + D        # Logout / EOF
Ctrl + L        # Clear screen
clear           # Clear terminal
history         # Show command history
!!
               # Repeat last command

```
