# Threat Hunting with AC Hunter

## Objective
Analyze packet captures to identify potential Indicators of Compromise (IOCs) using Active Countermeasures' AC-Hunter Community Edition tool.

## Tools Used
- AC-Hunter Community Edition
- Zeek
- RITA
- Virus Total
- AbuseIPDB
- User Agent String Parsing Tool

### Acknowledgements
The PCAPs in the following exercises are from [Chris Brenton's Cyber Threat Hunting Level 1 training](https://www.activecountermeasures.com/hunt-training/) as well as [Active Countermeasures' Malware of the Day blog](https://www.activecountermeasures.com/category/malware-of-the-day/).

## What is Threat Hunting
Cyber threat hunting is a proactive approach to network security focused on actively searching for and identifying potential security threats and adversaries within an organization's network infrastructure. Unlike traditional cybersecurity measures that primarily rely on automated security tools and systems to detect known threats, threat hunting involves human-driven analysis and investigation to uncover unknown or stealthy threats that may evade detection by automated systems. This proactive approach enables organizations to reduce the gap between the failure of security controls and the initiation of response measures, significantly reducing damage or the disruption business operations.

## What Are We Searching for When Threat Hunting?
Because malware is often controlled from a remote host, our focus will be on targeting potential Command & Control (C2) operations. This involves identifying persistent outbound connections and abnormal protocol behaviour, verifying the business necessity of each connection, conducting reputation checks on external IP addresses, and investigating internal IP addresses as needed to determine follow-up actions, such as safelisting external IPs or triggering the incident response process.

## PCAP #1
###### Importing the zeek logs with RITA to analyze in the AC-Hunter web interface
![](img/rita.png) <br>
###### AC-Hunter Dashboard displaying 100% threat rating based on the criteria in "Threat Activity"
![](img/ac2.png) <br>
###### The Beacon Web module displaying all outbound connections with above 50% threat rating
![](img/ac3.png) <br>
###### Safelisting the Microsoft delivery optimization host typically used for patching
![](img/safe1.png) <br>
###### Filtering the Beacon Web module to display the remaining connections with above an 80% threat rating
![](img/ac4.png) <br>
###### Safelisting another Windows patching host
![](img/safe2.png) <br>
###### The Beacon Web module displaying the two remaining connections with above an 80% threat rating
![](img/ac5.png) <br>
###### Safelisting the Windows Tile Service connection
![](img/safe3.png) <br>
###### Safelist Overview
![](img/safe4.png) <br>
###### The remaining outbound connection with a threat rating above 80%
![](img/ac6.png) <br>
###### The Deep Dive module displaying statistics for the above connection
![](img/ac7.png) <br>
###### Taking a look at the Long Connections module (Duration > 5 hours)
![](img/ac8.png) <br>
###### The Deep Dive module displaying statistics for the above connection
![](img/ac9.png) <br>
###### The Deep Dive module displaying statistics for the above connection (Standard Windows Service)
![](img/ac10.png) <br>
###### Further investigation of our remaining outbound connection above 80% within the Client Signatures module
![](img/acua.png) <br>
###### Windows 7 User Agent String which is inconsistent with other connections in the environment
![](img/ua1.png) <br>
###### No entries on Virus Total (This doesn't mean we're in the clear!)
![](img/vt1.png) <br>
###### There were no FQDN queries for this suspicious IP prior to the connection
![](img/zeek.png) <br>
###### All 3011 connection include the string seen below
![](img/zeek2.png) <br>

### Conclusion
The connections to 104[.]248.234.238 are suspicious due to the following:
- There were no FQDN queries before the connections were made
- There were over 3,000 connections diplaying beacon-like attributes
- The user agent string shifted to Windows 7 from Windows 10
- All connections include the long random string seen above begining with "rmvk30g"
- "rmvk30g" in URIs is known to be associated with the Fiesta Exploit Kit 
## PCAP #2
######
![](img/ac11.png) <br>
######
![](img/ac12.png) <br>
######
![](img/dns.png) <br>
######
![](img/dns2.png) <br>
### Conclusion

## PCAP #3
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
### Conclusion
