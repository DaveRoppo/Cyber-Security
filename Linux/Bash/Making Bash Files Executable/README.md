1. Add shebang line to the first line of the file “#!/bin/bash”
   - The shebang line is the absolute path to the bash interpreter, this ensures the script will be interpreted with bash regardless of the shell
   - does the script need to end with *.sh*? (it is reccomended to store executbles with no .sh extension)
      
2. use command "chmod u+x *scriptname* to make the file executable 
   - *chmod u+x* vs *chmod +x*? (the “u” gives only the owner permission to execurte the file, whereas leaving it out gives all users premission to exe)
      
3. Move/place script in the /usr/local/bin directory (this should already be added to path)
   - This allows you to run the script as *scriptname* instead of *./scriptname*
      
4. Run script with command *scriptname* 

![image](https://user-images.githubusercontent.com/58571770/186506013-77b76f1c-506e-4147-80e6-90b53d9cc2e3.png)



