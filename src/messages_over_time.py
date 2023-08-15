# The script sets the file path for the packet capture file and the TShark executable path. It opens the capture file
# using PyShark and initializes lists to store timestamps and packet lengths. The script iterates through each packet
# in the capture file. For each packet, it extracts the packet's timestamp and appends it to the timestamps list. It
# also extracts the length of the packet and appends it to the packet_lengths list. After processing all packets,
# the packet capture is closed. The script then converts the timestamps to relative time in seconds by subtracting
# the first timestamp from each subsequent timestamp. Finally, the script uses Matplotlib to create a bar plot
# showing the packet lengths against the relative time in seconds. In summary, this code analyzes network packet data
# to plot how the packet lengths change over time using a bar plot. It extracts timestamps and packet lengths from
# the packet capture file and converts the timestamps to relative time for better visualization.
import pyshark
import matplotlib.pyplot as plt

# Path to the packet capture file
capture_file = '/home/vivian/group_7.pcapng'

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
