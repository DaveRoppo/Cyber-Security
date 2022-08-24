# System Maintainence:

* sudo apt update -y && sudo apt upgrade -y * - Updates and upgrades the system

sudo apt autoremove -y - Removes packages that are no longer required

sudo apt install (package name)  - installs the specified package

# Navigation:

pwd - display current working directory ("Print Working Directory")

cd - Change directory 

cd (path/) - Navigate to a specific directory

cd .. - Navigate one directory back (Parent Directory of current working directory)

ls - List files & directories in the current working directory

ls -la - List all hidden files in the current wokring directory
# Creating/Modifying/Viewing/Finding Files & Directories:

touch (file name) - Creates an empty file with a name of your choosing

cat (file name) - writes file contents to the terminal

echo () > (file name) - writes whatever you specify to the file name you specify

nano (file name) - Opens the specifies file in the nano text editor

vim (file name) - Opens the specifies file in the vim text editor

mkdir (directory name) - creates a directory with whatever name you specify

mv (file name) (directory name) - moves a file into a specified directory

cp (file name) (new file name) - Copies the contents of (file name) to (new file name)

rm (file name) - Deletes the file (Use caution)

rm (directory name) -r - Deletes a directory and its contents

tr  - Similar to find & replace in Microsoft word 

find (directory) -iname (filename) 2>/dev/null - Searches the specified directory for files matching the specified name (case insensitive) and redirects errors so that they are not displayed in the terminal

which (program name) - great for determining if a specific program is on the system or not

sed - Similar to tr, but can search and replace more specific strings

find (directory) *word* -name - 

chmod - modify file permissions (read, write, execute)

tree -L 1 / -  Displays the 1st Level of the directory tree starting at / (root)

# Searching & Sorting:
grep 'word' (filename) - search files for plaintext strings using regular expressions 

sort (filename)- sort data within a file (without any options, sort will default to sorting alphabetically, numbers ahead of letters)

# Networking:

ifconfig - Displays all netowork interfaces and associated IP & MAC adresses

ssh username@IP - Secure Shell (SSH) is a network protocol administrators often use to remotely access another computer securely over an unsecured network

# Help:

man (command) - Displays the associated manual page for the specified command

(command) -h - Displays information about the specified command

 



