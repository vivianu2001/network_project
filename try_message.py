import pyshark
import matplotlib.pyplot as plt
from datetime import datetime

# Path to the packet capture file
capture_file = '/home/vivian/try1.pcapng'

# Set the TShark path
tshark_path = '/usr/bin/tshark'

# Open the capture file and specify the TShark path
cap = pyshark.FileCapture(capture_file, tshark_path=tshark_path)

# Initialize lists to store event information
event_times = []
event_lengths = []
threshold = 0.1
# seconds, choose a suitable value based on your data

# Iterate through the packets
burst_start_time = None
for packet in cap:
    try:
        # Extract the timestamp and length of the packet
        timestamp = packet.sniff_time.timestamp()
        length = int(packet.length)

        if burst_start_time is None:
            # First packet in the burst
            burst_start_time = timestamp

        # Check if the inter-packet delay is greater than the threshold
        if timestamp - burst_start_time > threshold:
            # The burst is complete, store the event information
            event_times.append(datetime.fromtimestamp(burst_start_time).strftime('%H:%M'))
            event_lengths.append(length)

            # Reset for the next burst
            burst_start_time = timestamp

    except (KeyError, ValueError) as e:
        # Skip packets that do not contain relevant information
        continue

# Close the packet capture
cap.close()

# Plot the event lengths against event times
plt.figure(figsize=(10, 6))
plt.bar(event_times, event_lengths, width=0.1, color='b')
plt.xlabel('Time')
plt.ylabel('Event Length (bytes)')
plt.title('Event Lengths over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
