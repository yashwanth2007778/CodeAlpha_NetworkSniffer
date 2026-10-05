# CodeAlpha Network Sniffer

## Internship Task 1 – Basic Network Sniffer

This project is developed as part of the CodeAlpha Cyber Security Internship.

The Network Sniffer is a Python-based tool that captures network packets and displays important information such as source IP address, destination IP address, protocol, port numbers, timestamp, and limited payload information.

## Objective

The main objective of this project is to understand how network packets can be captured and analyzed using Python.

## Features

- Captures network packets in real time
- Displays source IP address
- Displays destination IP address
- Identifies network protocols
- Supports TCP, UDP, and ICMP packets
- Displays source and destination ports for TCP/UDP
- Displays timestamp for each captured packet
- Displays limited payload information
- Counts captured packets
- Provides protocol statistics
- Handles packet capture interruption safely

## Technologies Used

- Python
- Scapy
- Npcap
- VS Code

## Requirements

- Python 3.x
- Scapy
- Npcap (for Windows packet capture)

## Installation

### 1. Install Python

Download and install Python 3.x.

Make sure Python is added to the system PATH.

### 2. Install Scapy

Open Command Prompt or VS Code Terminal and run:

```bash
pip install scapy