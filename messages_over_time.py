import pyshark
import matplotlib.pyplot as plt

# Path to the packet capture file
capture_file = '/home/vivian/clean_chat_2_people.pcapng'

# Set the TShark path
tshark_path = '/usr/bin/tshark'

# Open the capture file and specify the TShark path
cap = pyshark.FileCapture(capture_file, tshark_path=tshark_path)

# Initialize lists to store timestamps and packet lengths
timestamps = []
packet_lengths = []

# Iterate through the packets
for packet in cap:
    # Extract the timestamp of the packet
    timestamp = packet.sniff_time
    timestamps.append(timestamp)

    # Extract the length of the packet
    length = int(packet.length)
    packet_lengths.append(length)

# Close the packet capture
cap.close()

# Convert timestamps to relative time in seconds
timestamps_sec = [(ts - timestamps[0]).total_seconds() for ts in timestamps]

# Plot the packet lengths against time
plt.figure(figsize=(10, 6))
plt.bar(timestamps_sec, packet_lengths)
plt.xlabel('Time (seconds)')
plt.ylabel('Packet Length (bytes)')
plt.title('Packet Length over Time')
plt.show()
