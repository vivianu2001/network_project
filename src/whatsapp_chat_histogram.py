#    The script sets the path to the WhatsApp chat text file and imports the required libraries.
#    It initializes empty lists timestamps and imds to store timestamps and inter-message delays, respectively.
#    The script reads the chat text file and extracts lines from it.
#    For each line, it tries to extract the timestamp part and convert it to a datetime object.
#    The timestamps are appended to the timestamps list. If a line doesn't match the expected format, it is skipped.
#    After extracting timestamps, the script calculates inter-message delays by finding the time difference between consecutive timestamps.
#    The inter-message delays are stored in the imds list.
#    The script then proceeds to plot a histogram of the inter-message delays using Matplotlib.
#    It plots the histogram with 30 bins, normalized to form a probability density function (PDF).
#    Additionally, it fits an exponential distribution to the inter-message delays to model the data.
#    The fitted exponential distribution is plotted as a red curve on top of the histogram.
#    The plot is labeled with appropriate titles and axis labels.
#    Finally, the plot is displayed using plt.show().
#In summary, this code analyzes a WhatsApp chat text file, extracts timestamps from the messages, calculates inter-message delays, and visualizes the distribution of these delays as a histogram. It also fits an exponential distribution to the inter-message delays for modeling purposes.

import datetime
import matplotlib.pyplot as plt
import numpy as np

# Path to the WhatsApp chat text file
chat_file = '/home/vivian/Downloads/algo2.txt'

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
