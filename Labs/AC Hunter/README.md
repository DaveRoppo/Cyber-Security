# Threat Hunting with AC Hunter

## Objective
Analyze packet captures to identify potential Indicators of Compromise (IOCs) using Active Countermeasures' AC-Hunter Community Edition tool.

## Tools Used
- AC-Hunter Community Edition
- Zeek
- RITA
- Virus Total
- AbuseIPDB
- User Agent Tool

### Acknowledgements
The PCAPs in the following exercises are from [Chris Brenton's Cyber Threat Hunting Level 1 training](https://www.activecountermeasures.com/hunt-training/) as well as [Active Countermeasures' Malware of the Day blog](https://www.activecountermeasures.com/category/malware-of-the-day/).

## What is Threat Hunting
Cyber threat hunting is a proactive approach to network security focused on actively searching for and identifying potential security threats and adversaries within an organization's network infrastructure. Unlike traditional cybersecurity measures that primarily rely on automated security tools and systems to detect known threats, threat hunting involves human-driven analysis and investigation to uncover unknown or stealthy threats that may evade detection by automated systems. This proactive approach enables organizations to reduce the gap between the failure of security controls and the initiation of response measures, significantly reducing damage or the disruption business operations.

## What Are We Searching for When Threat Hunting?
Because malware is often controlled from a remote host, our focus will be on targeting potential Command & Control (C2) operations. This involves identifying persistent outbound connections and abnormal protocol behaviour, verifying the business necessity of each connection, conducting reputation checks on external IP addresses, and investigating internal IP addresses as needed to determine follow-up actions, such as safelisting external IPs or triggering the incident response process.

### PCAP #1
######
![](img/rita.png) <br>
######
![](img/ac2.png) <br>
######
![](img/ac3.png) <br>
######
![](img/ac4.png) <br>
######
![](img/ac5.png) <br>
######
![](img/ac6.png) <br>
######
![](img/ac7.png) <br>
######
![](img/ac8.png) <br>
######
![](img/ac9.png) <br>
######
![](img/ac10.png) <br>
######
![](img/acua.png) <br>
######
![](img/ua1.png) <br>
######
![](img/safe1.png) <br>
######
![](img/safe2.png) <br>
######
![](img/safe3.png) <br>
######
![](img/safe4.png) <br>
######
![](img/vt1.png) <br>
######
![](img/zeek.png) <br>
######
![](img/zeek2.png) <br>

### PCAP #2
######
![](img/ac11.png) <br>
######
![](img/ac12.png) <br>
######
![](img/dns.png) <br>
######
![](img/dns2.png) <br>

### PCAP #3
######
![](img/ac13.png) <br>
######
![](img/ac14.png) <br>
######
![](img/ac15.png) <br>
######
![](img/safe5.png) <br>
######
![](img/ua2.png) <br>
######
![](img/vt2.png) <br>
######
![](img/ac_cobalt.png) <br>
