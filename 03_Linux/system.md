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
---
---
---
---


```
# KZ Insight - Parrot OS Initial Setup Guide

#############################################
# 1. تحديث النظام
#############################################

sudo apt update
# تحديث قائمة الحزم

sudo apt upgrade -y
# تحديث البرامج المثبتة

sudo apt full-upgrade -y
# تحديث كامل للنظام والنواة إن وجدت

sudo apt autoremove -y
# حذف الحزم غير المستخدمة

sudo apt autoclean
# تنظيف ملفات التثبيت القديمة


#############################################
# 2. تثبيت أدوات VMware
#############################################

sudo apt install -y open-vm-tools open-vm-tools-desktop
# تثبيت أدوات VMware (النسخ واللصق - دقة الشاشة - الماوس)

systemctl status open-vm-tools
# التأكد أن الخدمة تعمل

systemctl status vmtoolsd
# التأكد أن خدمة VMware تعمل

vmware-toolbox-cmd -v
# معرفة إصدار VMware Tools

vmware-user &
# تشغيل خدمة المستخدم الخاصة بـ VMware


#############################################
# 3. معرفة معلومات النظام
#############################################

neofetch
# عرض معلومات الجهاز (إذا كان مثبتاً)

hostnamectl
# معلومات النظام

cat /etc/os-release
# إصدار النظام

uname -a
# إصدار النواة

hostname
# اسم الجهاز

hostname -I
# عنوان IP

whoami
# المستخدم الحالي

pwd
# المجلد الحالي


#############################################
# 4. معرفة معلومات الهارد والذاكرة
#############################################

lsblk
# الأقراص

df -h
# المساحة المستخدمة

du -sh ~
# حجم مجلد المستخدم

free -h
# استخدام الرام

lscpu
# معلومات المعالج


#############################################
# 5. الشبكات
#############################################

ip a
# كروت الشبكة

ip route
# جدول التوجيه

ping google.com
# اختبار الإنترنت


#############################################
# 6. إدارة الحزم
#############################################

apt search package

sudo apt install package

sudo apt remove package

sudo apt purge package

sudo apt autoremove


#############################################
# 7. تثبيت Google Chrome
#############################################

cd ~/Downloads

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo apt install ./google-chrome-stable_current_amd64.deb

google-chrome


#############################################
# 8. تثبيت Visual Studio Code
#############################################

sudo apt install code

# إذا لم يكن موجوداً بالمستودعات:

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list

sudo apt update

sudo apt install code


#############################################
# 9. تثبيت Git
#############################################

sudo apt install git

git --version

git config --global user.name "Jamal Salem"

git config --global user.email "you@example.com"


#############################################
# 10. تثبيت Python
#############################################

sudo apt install python3 python3-pip

python3 --version

pip3 --version


#############################################
# 11. تثبيت أدوات البرمجة
#############################################

sudo apt install build-essential

gcc --version

g++ --version

make --version


#############################################
# 12. أوامر الملفات
#############################################

ls

ls -la

cd

mkdir Project

touch file.txt

cp file.txt backup.txt

mv file.txt folder/

rm file.txt

rm -rf folder/


#############################################
# 13. أوامر البحث
#############################################

find . -name "*.py"

grep "text" file.txt


#############################################
# 14. إدارة العمليات
#############################################

ps aux

top

htop

kill PID

kill -9 PID


#############################################
# 15. الخدمات
#############################################

systemctl status service

sudo systemctl restart service

sudo systemctl enable service

sudo systemctl disable service


#############################################
# 16. جلسة سطح المكتب
#############################################

echo $XDG_SESSION_TYPE

echo $XDG_CURRENT_DESKTOP

# يجب أن يكون:

Plasma (X11)

# وليس

Wayland

# لأن VMware يعمل بصورة أفضل مع X11.


#############################################
# 17. معرفة المنافذ
#############################################

ss -tuln

netstat -tulnp


#############################################
# 18. تحميل الملفات
#############################################

wget URL

curl -O URL


#############################################
# 19. الضغط وفك الضغط
#############################################

zip -r archive.zip folder

unzip archive.zip

tar -czvf archive.tar.gz folder

tar -xzvf archive.tar.gz


#############################################
# 20. إيقاف وإعادة تشغيل
#############################################

reboot

shutdown now

poweroff


#############################################
# 21. اختصارات الطرفية
#############################################

Ctrl + C
# إيقاف الأمر

Ctrl + L
# تنظيف الشاشة

Ctrl + D
# تسجيل خروج

history
# سجل الأوامر

!!
# إعادة تنفيذ آخر أمر

clear
# تنظيف الطرفية


#############################################
# ملاحظات مشروع KZ Insight
#############################################

✓ النظام: Parrot OS
✓ سطح المكتب: KDE Plasma
✓ الجلسة الموصى بها: X11
✓ VMware Tools مثبتة
✓ VS Code
✓ Git
✓ Python
✓ Build Essentials
✓ Google Chrome
✓ جاهز لبدء تطوير مشروع KZ Insight
