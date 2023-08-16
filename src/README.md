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

All the scripts in this repository follow a similar structure:

1. Opens the specified packet capture file using PyShark.
2. Initializes lists to store burst information, including burst times and lengths.
3. Iterates through each packet in the capture file, extracting timestamp and length information.
4. Calculates the inter-packet delay and groups packets into bursts based on a threshold.
5. Stores burst information in lists and closes the packet capture file.
6. Uses Matplotlib to create a bar plot showing burst lengths against their corresponding times.

## Configuration

In each script, you can configure the following variables:

- `capture_file`: Path to the packet capture file you want to analyze.
- `tshark_path`: Path to the TShark executable (if not in default system path).
- `threshold`: Inter-packet delay threshold for identifying bursts (in seconds).

## Result

After running a script, a bar plot will be displayed using Matplotlib. This plot visualizes burst lengths against their corresponding times, helping you understand burst traffic patterns in the network packet data. Burst lengths are displayed in megabytes (MB).

## Example Result

![Example Result](https://github.com/vivianu2001/network_project/assets/118671563/483a61ae-f1d5-4ba6-a8fb-0c0964da7598)
