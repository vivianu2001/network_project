
# Burst Length Analysis using PyShark and Matplotlib

This Python script analyzes burst lengths in a packet capture file using PyShark, a wrapper for TShark (Wireshark command-line tool). It then visualizes the burst lengths over time using Matplotlib.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- PyShark
- Matplotlib

You can install the required packages using `pip` with the following command:

```bash
pip install pyshark matplotlib
```

## Usage

1. Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/vivianu2001/event_extraction.git
cd event_extraction
```

2. Place your packet capture file (e.g., 'after_exam_clean.pcapng') in the project directory.

3. Open the `burst_length_analysis.py` script in a text editor and set the correct paths:

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
python burst_length_analysis.py
```

6. The script will process the packet capture file and display a bar plot showing burst lengths over time.

## Acknowledgments

- [PyShark](https://github.com/KimiNewt/pyshark) - PyShark is a wrapper for TShark, written in Python.
- [Matplotlib](https://matplotlib.org/) - Matplotlib is a plotting library for Python.

