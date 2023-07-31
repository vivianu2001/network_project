import datetime
import matplotlib.pyplot as plt
import numpy as np

# Path to the WhatsApp chat text file
chat_file = '/home/vivian/Downloads/automata_chat.txt'

timestamps = []
imds = []

# Read the chat text file
with open(chat_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Iterate over the lines and extract timestamps
for line in lines:
    try:
        # Split the line into timestamp and message parts
        parts = line.split('] ')

        # Extract the timestamp string and convert it to a datetime object
        timestamp_str = parts[0][1:]
        timestamp = datetime.datetime.strptime(timestamp_str, '%d/%m/%Y, %H:%M:%S')

        timestamps.append(timestamp)
    except ValueError:
        # Skip lines that do not match the expected format
        continue

# Calculate inter-message delays
for i in range(1, len(timestamps)):
    imd = (timestamps[i] - timestamps[i - 1]).total_seconds()
    imds.append(imd)

# Plot the histogram of inter-message delays
plt.figure(figsize=(10, 6))
plt.hist(imds, bins=30, density=True, alpha=0.7, label='Histogram of Inter Message Delays')

# Fit an exponential distribution
fit_x = np.linspace(0, max(imds), 1000)
lambda_ = 1 / np.mean(imds)  # Estimated lambda for the exponential distribution
fit_y = lambda_ * np.exp(-lambda_ * fit_x)

# Plot the fitted exponential distribution
plt.plot(fit_x, fit_y, 'r', label='Fitted Exponential Distribution')

plt.xlabel('Inter Message Delays (Seconds)')
plt.ylabel('PDF')
plt.title('Histogram of Inter Message Delays with Fitted Exponential Distribution')
plt.legend()
plt.show()
