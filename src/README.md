# Practical Traffic Analysis Attacks on Secure Messaging Applications

This project focuses on practical traffic analysis techniques for studying network traffic in secure messaging applications. It includes two Python scripts that analyze network traffic data and messaging patterns:

## Burst Length Analysis using PyShark and Matplotlib(event_extraction.py)

The Burst Length Analysis script analyzes burst lengths in a packet capture file using PyShark, a wrapper for TShark (Wireshark command-line tool). It then visualizes the burst lengths over time using Matplotlib.

### Description

The Burst Length Analysis script focuses on studying burst patterns in network traffic using packet capture data. It calculates burst lengths by analyzing the inter-packet delays in a given packet capture file. The analysis is done with the help of PyShark, which provides a convenient interface to work with TShark for processing network traffic data.

### Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- PyShark
- Matplotlib

You can install the required packages using `pip` with the following command:

```bash
pip install pyshark matplotlib
```

### Usage

1. Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/vivianu2001/event_extraction.py.git
cd event_extraction.py
```

2. Place your packet capture file in the project directory.
3. Open the `event_extraction.py` script in a text editor and set the correct paths:

```python
# Path to the packet capture file
capture_file = '/path/to/your/capture/file.pcapng'

# Set the TShark path
tshark_path = '/path/to/tshark'
```

Replace `/path/to/your/capture/file.pcapng` with the path to your packet capture file and `/path/to/tshark` with the path to your TShark executable.

4. Set the threshold value for burst identification:

```python
threshold = 0.00001  # seconds, choose a suitable value based on your data
```

Adjust the threshold value based on the characteristics of your packet capture data. The threshold defines the maximum inter-packet delay within a burst.

5. Run the script:

```bash
python event_extraction.py
```

6. The script will process the packet capture file and display a bar plot showing burst lengths over time.

## WhatsApp Inter-Message Delay Analysis using Matplotlib and Numpy(whatsapp_chat_histogram.py)

The WhatsApp Inter-Message Delay Analysis script analyzes inter-message delays in a WhatsApp chat text file and plots a histogram with a fitted exponential distribution using Matplotlib and Numpy.

### Description

The WhatsApp Inter-Message Delay Analysis script focuses on studying the delays between consecutive messages in a WhatsApp chat. It extracts timestamps from the chat text file and calculates the inter-message delays. The analysis involves plotting a histogram and fitting an exponential distribution to the delays to understand the messaging patterns.

### Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Matplotlib
- Numpy

You can install the required packages using `pip` with the following command:

```bash
pip install matplotlib numpy
```

### Usage

1. Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/vivianu2001/whatsapp_chat_histogram.py.git
cd whatsapp_chat_histogram.py
```

2. Place your WhatsApp chat text file in the project directory.

3. Open the `whatsapp_chat_histogram.py` script in a text editor and set the correct path:

```python
# Path to the WhatsApp chat text file
chat_file = '/path/to/your/whatsapp/chat/file.txt'
```

Replace `/path/to/your/whatsapp/chat/file.txt` with the path to your WhatsApp chat text file.

4. Run the script:

```bash
python whatsapp_chat_histogram.py
```

5. The script will process the WhatsApp chat text file, calculate inter-message delays, plot a histogram, and fit an exponential distribution to the delays.


# Messages Over Time Analysis(messages_over_time)

This script is designed to analyze a packet capture file using PyShark and visualize the packet lengths over time using Matplotlib. The packet capture file should be in the PCAP format (e.g., `.pcap`, `.pcapng`).

## Requirements

- Python 3.x
- PyShark (Python wrapper for TShark)
- Matplotlib

Make sure you have installed the necessary libraries before running the script.

## Usage

1. Ensure you have installed Python 3.x on your system.

2. Install the required Python libraries using `pip`:

```bash
pip install pyshark matplotlib
```

3. Update the `capture_file` and `tshark_path` variables in the script:

```python
# Path to the packet capture file
capture_file = '/path/to/your/capture/file.pcapng'

# Set the TShark path (if not in the default location)
tshark_path = '/path/to/tshark'
```

Replace `/path/to/your/capture/file.pcapng` with the path to your packet capture file.

4. Run the script:

```bash
python messages_over_time.py
```

5. The script will read the packet capture file and extract the timestamps and lengths of each packet. It will then convert the timestamps to relative time in seconds (relative to the first packet's timestamp).

6. The output will be a plot displaying the packet lengths against time in seconds. The plot will pop up on your screen, or you can save it programmatically if needed.

## Note

- Ensure that you have appropriate permissions to read the packet capture file.

- If TShark is not in the default location (`/usr/bin/tshark`), provide the correct path to the `tshark_path` variable.

- Make sure the required libraries are installed and accessible in your Python environment.

- The script will display the plot interactively. If you wish to save the plot programmatically, you can use the `savefig` function from Matplotlib.

- This script is a basic example of packet capture analysis and visualization. You can extend and modify it based on your specific requirements.

- For larger capture files or performance optimization, you may need to consider using `tshark` directly via the command line for initial filtering and then process the filtered output with PyShark.

Happy analyzing!

---

You can copy and use this README directly for your `messages_over_time.py` script. Just make sure to modify the `capture_file` and `tshark_path` variables as needed before running the script.

## Acknowledgments
This project was inspired by the research paper "Practical Traffic Analysis Attacks on Secure Messaging Applications" by Alireza Bahramali.
Special thanks to the Scipy, NumPy, and Matplotlib communities for providing essential libraries for data analysis and visualization.


