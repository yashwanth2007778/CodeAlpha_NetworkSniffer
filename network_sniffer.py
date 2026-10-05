from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

# Packet statistics
packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0
other_count = 0


def process_packet(packet):
    global packet_count
    global tcp_count, udp_count, icmp_count, other_count

    if IP not in packet:
        return

    packet_count += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Identify protocol
    if TCP in packet:
        protocol = "TCP"
        tcp_count += 1

    elif UDP in packet:
        protocol = "UDP"
        udp_count += 1

    elif ICMP in packet:
        protocol = "ICMP"
        icmp_count += 1

    else:
        protocol = "Other"
        other_count += 1

    print("\n" + "=" * 60)
    print(f"Packet Number  : {packet_count}")
    print(f"Timestamp      : {timestamp}")
    print(f"Source IP      : {source_ip}")
    print(f"Destination IP : {destination_ip}")
    print(f"Protocol       : {protocol}")

    # Display port information
    if TCP in packet:
        print(f"Source Port    : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")

    elif UDP in packet:
        print(f"Source Port    : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    # Display limited payload information
    if packet.haslayer("Raw"):
        payload = packet["Raw"].load
        print(f"Payload Size   : {len(payload)} bytes")
        print(f"Payload Preview: {payload[:50]}")

    print("=" * 60)


def show_statistics():
    print("\n" + "=" * 60)
    print("NETWORK SNIFFER STATISTICS")
    print("=" * 60)
    print(f"Total Packets : {packet_count}")
    print(f"TCP Packets   : {tcp_count}")
    print(f"UDP Packets   : {udp_count}")
    print(f"ICMP Packets  : {icmp_count}")
    print(f"Other Packets : {other_count}")
    print("=" * 60)


print("=" * 60)
print("        CODEALPHA NETWORK SNIFFER")
print("=" * 60)
print("Starting packet capture...")
print("Press CTRL+C to stop the sniffer.")
print("=" * 60)

try:
    sniff(prn=process_packet, store=False, timeout=30)
    show_statistics()
except KeyboardInterrupt:
    print("\n\nPacket capture stopped by user.")
    show_statistics()

except Exception as error:
    print("\nAn error occurred:")
    print(error)