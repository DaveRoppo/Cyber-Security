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
![](img/sl1.png) <br>
### PCAP #2
### PCAP #3
