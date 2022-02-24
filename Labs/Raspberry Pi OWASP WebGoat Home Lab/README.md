*Disclaimer: "While running this program your machine will be extremely vulnerable to attack. You should disconnect from the Internet while using this program. WebGoat’s default configuration binds to localhost to minimize the exposure."*

## About

In this project, I will set up and run OWASP's WebGoat application in a docker container on my [Raspberry Pi 4 running Kali Linux](https://github.com/DaveRoppo/Cyber-Security/tree/main/Linux/Raspberry%20Pi/Kali%20Linux%20Install) to practice offensive security skills in an isolated environment.

## What is WebGoat?

"WebGoat is a deliberately insecure application that allows interested developers just like you to test vulnerabilities commonly found in Java-based applications that use common and popular open source components."

## What is Docker container?

"A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings."

## Installation 

#### Install Docker
```bash
kali@kali:~$ sudo apt update
kali@kali:~$
kali@kali:~$ sudo apt install -y docker.io
kali@kali:~$
kali@kali:~$ sudo systemctl enable docker --now
kali@kali:~$
kali@kali:~$ docker
kali@kali:~$
```
- Verify docker is installed and working correctly by running the following:
```bash
docker run hello-world
```
#### Install WebGoat
```bash
sudo docker pull cambarts/webgoat-8.0-rpi
```
#### Run WebGoat
```bash
sudo docker run -p 8080:8080 -t cambarts/webgoat-8.0-rpi
```
#### Access WebGoat
- In a web browser, navigate to RaspPI_IP_Address:8080/WebGoat and register for an account!

## Acknowledgements
- This project was inspired by Gerald Auger - Simply Cyber's Raspberry Pi Cybersecurity homelab
- [Kali Linux Docker Documentation](https://www.kali.org/docs/containers/installing-docker-on-kali/)
- [Docker containers explained](https://www.docker.com/resources/what-container)
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
