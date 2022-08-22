# About

In this project, I will create a Kali Linux ethical hacking homelab by setting up a virtual machine in Oracle VM VirtualBox.

# What is a Virtual Machine (VM)?

A virtual machine is a virtual environment created using physical hardware that operates like a physical machine with its own CPU, memory, networking, and storage. A software referred to as a hypervisor reserves portions of the physical machine's hardware for use by the virtual machine. 

# Why Kali Linux for Ethical Hacking?

According to Kali.org, Kali Linux is an open-source, Debian-based Linux distribution aimed at advanced Penetration Testing and Security Auditing. Kali Linux contains several hundred tools targeted towards various information security tasks, such as Penetration Testing, Security Research, Computer Forensics and Reverse Engineering. 

# 1) Download Oracle VM VirtualBox

### - Navigate to virtualbox.org 
### - Click "Download VirtualBox 6.1"

![](vb.jpg)
### - Select the appropriate VirtualBox package for your operating system

![](host.jpg)
### - Click "Next" to accept all default options during the installation process

# 2) Download Kali Linux

### - Navigate to kali.org
### - Click "Download"

![](kali1.jpg)
### - Select "Bare Metal" 

![](kali2.jpg)
### - Select the appropriate .iso image installer (64 bit or 32 bit) for your machine

![](kali3.jpg)

# 3) Create Virtual Machine 

### - Open the VirtualBox application
### - Select the blue "New" icon

![](vm1.jpg)
### - Name your virtual machine anything you would like, for "Type:" Select "Linux", for "Version:" Select "Debian (64 bit)"

![](vm3.jpg)
### - Allocate atleast 2GB of memory to your virtual machine (the more the merrier, however 2GB should work fine!)

![](vm4.jpg)
### - Select "Create Virtual Hard Disk Now" and Click "Create"

![](vm5.jpg)
### - Select "VDI (VirtualBox Disk Image)"

![](vm6.jpg)
### - Select "Dynamically Allocated" 

![](vm7.jpg)
### - Allocate atleast 8GB of storage to your virtual machine's hard disk

![](vm8.jpg)
### - On the VirtualBox Home page, Click the orange "Settings" icon

![](vm9.jpg)
### - Navigate to the "Storage" tab in the settings window

![](vm11.jpg)
### - Under "Controller: IDE", Right-Click "Empty" and Select "Remove", then Click the "Add optical drive" icon to the right of "Controller: IDE"

![](vm12.jpg)
### - Click "Add" and navigate to your Kali Linux .iso image that we downloaded earlier, then Click "Choose" followed by "OK" to exit settings

![](vm13.jpg)
![](vm14.jpg)
![](vm15.jpg)


# 4) Install Kali Linux 

### - Start the virtual machine to begin the installation process

![](ki1.jpg)
### - Choose your language, country, and keymap settings
### - Choose a hostname for your virtual machine

![](ki5.jpg)
### - Leave "Domain Name" blank and Click "Continue"

![](ki6.jpg)
### - Choose your Username & Password
### - Choose your Timezone
### - Select "Guided - Use Entire Disk" and Click "Continue"

![](ki10.jpg)
### - On the partition disks page, Click "Continue" four times to accept the default disk partitioning configuration

![](ki11.jpg)
![](ki12.jpg)
![](ki13.jpg)
![](ki14.jpg)
### - Sit back while the base sustem installs

![](ki15.jpg)
### - Accept the default software selections by Clicking "Continue"

![](ki16.jpg)
### - Allow the selected software to install (This one will take some time)

![](ki17.jpg)
### - Select "Yes" to install the GRUB boot loader and Click "Continue"

![](ki18.jpg)
### - Leave the default disk selected and Click "Continue"

![](ki19.jpg)
### - Allow the installation to finish and Click "Continue" to reboot your virtual machine

![](ki20.jpg)
![](ki21.jpg)
### - Login with your username and password you created earlier!

![](ki22.jpg)
![](post1.jpg)

# Additional Resources

### [Top Things to do After Installing Kali Linux](https://www.ceos3c.com/security/top-things-after-installing-kali-linux/)

