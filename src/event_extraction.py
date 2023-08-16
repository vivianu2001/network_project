# The script sets the file path for the packet capture file and the TShark executable path. It opens the capture file
# using PyShark and initializes lists to store burst information. The script iterates through each packet in the
# capture file. For each packet, it extracts the packet's timestamp and length and calculates the inter-packet delay.
# Based on the inter-packet delay, the script groups packets into bursts. If the inter-packet delay is below a
# certain threshold, the packet belongs to the current burst; otherwise, it starts a new burst. The script stores the
# burst times and corresponding burst lengths in lists. After processing all packets, the packet capture is closed.
# Finally, the script uses Matplotlib to create a bar plot showing the burst lengths against their corresponding
# times. In summary, this code analyzes network packet data to detect and visualize burst traffic patterns.
import pyshark
import matplotlib.pyplot as plt
from datetime import datetime

# Path to the packet capture file
capture_file = '/put/your/capture/file/path.pcapng'

# Set the TShark path
tshark_path = '/usr/bin/tshark'

# Open the capture file and specify the TShark path
cap = pyshark.FileCapture(capture_file, tshark_path=tshark_path)

# Initialize lists to store burst information
burst_times = []
burst_lengths = []
current_burst_length = 0
threshold = 0.0000001# seconds, choose a suitable value based on your data

# Iterate through the packets
prev_timestamp = None
for packet in cap:
    try:
        # Extract the timestamp and length of the packet
        timestamp = packet.sniff_time.timestamp()
        length = int(packet.length)

        if prev_timestamp is None:
            prev_timestamp = timestamp
            current_burst_length = length
            continue

        # Calculate inter-packet delay
        inter_packet_delay = timestamp - prev_timestamp

        # Check if the inter-packet delay is greater than the threshold
        if inter_packet_delay <= threshold:
            # Add the current packet length to the current burst
            current_burst_length += length
        else:
            # The burst is complete, store the burst information
            burst_times.append(datetime.fromtimestamp(prev_timestamp).strftime('%H:%M'))
            burst_lengths.append(current_burst_length)

            # Reset for the next burst
            prev_timestamp = timestamp
            current_burst_length = length

    except (KeyError, ValueError) as e:
        # Skip packets that do not contain relevant information
        continue

# Close the packet capture
cap.close()

# Plot the burst lengths against burst times
plt.figure(figsize=(10, 6))
plt.bar(burst_times, burst_lengths, width=0.1, color='b')
plt.xlabel('Time')
plt.ylabel('Burst Length (bytes)')
plt.title('Burst Lengths over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
