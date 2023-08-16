# Network Project Scripts

This repository contains Python scripts utilized in our network project. These scripts are designed to analyze network traffic data, detect burst traffic patterns, and visualize packet sizes' Complementary Cumulative Distribution Function (CCDF). The scripts utilize libraries such as PyShark and Matplotlib to process packet capture files and generate visualization graphs.

## Prerequisites

Before using these scripts, ensure you have the following:

- Python 3.x installed.
- The PyShark and Matplotlib libraries. You can install them using the following command:
  ```
  pip install pyshark matplotlib
  ```

## Script Overview

All the scripts in this repository follow a similar structure, aiming to analyze and visualize network traffic data.

1. **event_extraction.py**: Analyzes network packet data to detect and visualize burst traffic patterns. Uses PyShark and Matplotlib libraries. Burst lengths are displayed in bytes.

2. **event_extraction_MB.py**: Similar to `event_extraction.py`, but burst lengths are displayed in megabytes (MB).

3. **messages_over_time.py**: Captures packet length over time to visualize the traffic pattern for a specific group.

4. **message_size_distribution_ccdf.py**: Captures packets to generate a graph showing the Complementary Cumulative Distribution Function (CCDF) of packet sizes.

5. **whatsapp_chat_histogram.py**: Reads a WhatsApp chat text file and extracts inter-message delay information. Creates a histogram to visualize the distribution of inter-message delays. Fits an exponential distribution to the inter-message delays.

## Configuration

In each script, you can configure variables to specify the input data file, thresholds, and other parameters required for analysis and visualization. Note that in **whatsapp_chat_histogram.py**, you'll need to replace the chat data with your own exported WhatsApp chat.

## Example Results

![Example Result event_extraction.py ](https://github.com/vivianu2001/network_project/assets/118671563/483a61ae-f1d5-4ba6-a8fb-0c0964da7598)
![Example Result messages_over_time.py](https://github.com/vivianu2001/network_project/assets/118671563/db663846-2456-4e18-8a70-8566a26ebb7c)
![Example Result message_size_distribution_ccdf.py](https://github.com/vivianu2001/network_project/assets/118671563/2a2f9b2a-b3a6-4d1c-a740-2c8de1073822)
![Example Result message_size_distribution_ccdf.py](https://github.com/vivianu2001/network_project/assets/118671563/2a2f9b2a-b3a6-4d1c-a740-2c8de1073822)
![Example Result whatsapp_chat_histogram.py](https://github.com/vivianu2001/network_project/assets/118671563/db735678-1f58-4ea2-906c-672b91f71b68)

