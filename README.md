# CodeAlpha Network Sniffer

## Internship Task – Basic Network Sniffer

This project is developed as part of the **CodeAlpha Cyber Security Internship**.

The Network Sniffer is a Python-based tool that captures network packets and displays important information such as source IP address, destination IP address, protocol, port numbers, timestamp, payload size, and a limited payload preview.

## Objective

The main objective of this project is to understand how network packets can be captured, inspected, and analyzed using Python and Scapy.

## Features

* Captures network packets in real time
* Displays source IP address
* Displays destination IP address
* Identifies network protocols
* Supports TCP, UDP, and ICMP packets
* Displays source and destination ports for TCP/UDP packets
* Displays timestamp for each captured packet
* Displays payload size
* Displays a limited payload preview
* Counts captured packets
* Provides protocol statistics
* Handles packet capture interruption safely

## Technologies Used

* Python 3
* Scapy
* Npcap
* Visual Studio Code

## Requirements

Before running the project, make sure you have:

* Python 3.x
* Scapy
* Npcap (required for packet capture on Windows)
* Administrator privileges may be required for packet capture

## Installation

### 1. Install Python

Download and install Python 3.x.

Make sure **Add Python to PATH** is selected during installation.

### 2. Install Scapy

Open PowerShell or Command Prompt and run:

```bash
pip install scapy
```

### 3. Install Npcap

Install Npcap on Windows and allow it to be used for packet capture.

## How to Run

Open PowerShell in the project directory:

```powershell
cd "C:\Users\ravin\OneDrive\CodeAlpha_NetworkSniffer"
```

Run the sniffer:

```powershell
python network_sniffer.py
```

The program will start capturing network packets and display information such as:

* Packet number
* Timestamp
* Source IP
* Destination IP
* Protocol
* Source port
* Destination port
* Payload size
* Payload preview

Press **Ctrl + C** to stop packet capture and display the final statistics.

## Example Output

```text
============================================================
Packet Number  : 117
Timestamp      : 2026-10-05 16:59:17
Source IP      : 10.16.220.85
Destination IP : 10.16.220.209
Protocol       : TCP
Source Port    : 53
Destination Port: 64361
Payload Size   : 91 bytes
Payload Preview: ...
============================================================
```

## Screenshots

### Network Sniffer Running

![Network Sniffer Running](screenshots/01-sniffer-running.png)

### Network Sniffer Statistics

![Network Sniffer Statistics](screenshots/02-statistics.png)

## Project Structure

```text
CodeAlpha_NetworkSniffer/
│
├── network_sniffer.py
├── README.md
└── screenshots/
    ├── 01-sniffer-running.png
    └── 02-statistics.png
```

## Learning Outcomes

Through this project, I learned:

* Basics of network packet capture
* How IP addresses and ports are used in network communication
* How TCP, UDP, and ICMP traffic can be identified
* How to use Scapy for packet analysis
* How to display and analyze packet information using Python
* Basic Git and GitHub project management

## Disclaimer

This project is developed for **educational and cybersecurity learning purposes**. Network packet capture should only be performed on networks and systems where you have permission to monitor the traffic.

## Author

**Yashwanth Sirimalla**

Developed as part of the **CodeAlpha Cyber Security Internship**.
