## About

In this project, I will set up a vulnerable virtual machine using Metasploitable and Oracle VM Virtual Box on Windows 11. 

## Process
#### 1) Register & Download Metasploitable 
https://information.rapid7.com/download-metasploitable-2017.html?LS=1631875&CS=web

#### 2) Open Oracle VM VirtualBox

![](meta1.jpg)
#### 3) Click the Blue "New" Icon to create a new Virtual Machine & Fill out "Type:" and "Version:" Fields as shown below, Click "Next"

![](meta2.jpg)
#### 4) Accept the default memory recommended size of 512 MB by Clicking "Next"

![](meta3.jpg)
#### 5) Select "Use an existing virtual hard disk file" & Click the "Browse" Icon

![](meta4.jpg)
#### 6) In the "Hard Disk Selector" window, Click "Add"

![](meta5.jpg)
#### 7) Navigate to the "Metasploitable.vmdk" that you downloaded in Step 1, once it's displayed in the window, Select it and Click "Choose"

![](meta6.jpg)
#### 8) On the "Hard Disk" window, Select "Use an existing virtual hard disk file" & Select "Metasploitable.vmdk" from the dropdown, Click "Create"

![](meta7.jpg)
#### 9) From the VirtualBox home screen, Select the Green "Start" icon and Metasploitable will begin installing; Once finished, you will be greeted with a login screen

![](meta10.jpg)
#### 10) Click "Enable Adapter & In the dropdown next to "Attached to:", Select "Bridged Adapter"; In the "Name" dropdown, Select your adapter (This will result in the VM being on your local network) 



