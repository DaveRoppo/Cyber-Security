1. *sudo pacman -S rsync*

2. *lsblk*
   - find file path of your external drive

3. *sudo pacman -S cronie*

4. *crontab -e*
   - by default, crontab uses vim, to use it with nano, do the following:
      -*export VISUAL=nano*
      -*export EDITOR=nano*
      -This is only valid for the current session, to make it permanent, do the following:
      ![bash1](bash1.png)
         
5. *source ~/.bashrc*

6. *crontab -e* 
   - verify that it now opens in nano 

7. *sudo nano ~/scripts/cherry_backup*
![bash2](bash2.png)

8. *sudo chmod +x cherry_backup*


9. *crontab -e*
![bash3](bash3.png)

10. *sudo systemctl start cronie*

11. *sudo systemctl enable cronie* 

