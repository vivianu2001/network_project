# Practical Traffic Analysis Attacks on Secure Messaging Applications

This project focuses on practical traffic analysis techniques for studying network traffic in secure messaging applications. It includes two Python scripts that analyze network traffic data and messaging patterns:

## Burst Length Analysis using PyShark and Matplotlib

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

## WhatsApp Inter-Message Delay Analysis using Matplotlib and Numpy

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

## Acknowledgments

This project is based on the principles of Practical Traffic Analysis Attacks on Secure Messaging Applications, which explores various traffic analysis techniques, including inter-message delay analysis.

