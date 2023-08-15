# WhatsApp Traffic Analysis Project

This project is centered around the analysis of WhatsApp group conversations using practical traffic analysis techniques as presented in the article "Practical Traffic Analysis Attacks on Secure Messaging Applications." The primary aim of the project is to address key project questions while analyzing 7 distinct WhatsApp groups.

## Table of Contents

- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results](#results)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [References](#references)

## Introduction

The project is based on the "Practical Traffic Analysis Attacks on Secure Messaging Applications" article, focusing on answering project questions through the analysis of 7 WhatsApp groups. The analysis involves the recording of WhatsApp conversations using Wireshark and the implementation of the EVENT BASED DETECTOR algorithm detailed in the article.

## Methodology

1. Recorded WhatsApp Conversations: The conversations were captured using Wireshark to obtain network traffic data.
2. Implemented EVENT_EXTRACTION.PY: Using the EVENT BASED DETECTOR algorithm, the event_extraction.py script was created. It produces graphs that reveal the size and nature of messages within each WhatsApp group based on network packet information.
3. PDF and CCDF Graphs: Mathematical graphs were generated using `whatsapp_chat_histogram.py` for PDF functions and `message_size_distribution_ccdf.py` for CCDF functions. These tools allowed insights into message distribution patterns.

## Results

- Graphs for Message Sizes: The produced graphs under the `res` folder for each group (named `group_x_ee`) display the size of messages in each WhatsApp group based on network packet analysis.
- Message Over Time: `messeges_over_time` in the `res` folder for each group (named `group_x_mot`) illustrating package sizes over the duration of each group.
- PDF and CCDF Functions: `histogram_group_x` folder contains PDF graphs for groups with substantial message counts (groups 6 and 7), while CCDF graphs are produced using `message_size_distribution_ccdf.py`.

**Privacy Protection:** It's important to note that privacy protection for participants has been prioritized in this project. When generating the histogram graphs using `whatsapp_chat_histogram.py`, we do not upload or include the actual text message data. 

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/vivianu2001/network_project.git
   ```

2. Navigate to the repository directory:

   ```
   cd network_project
   ```

3. Explore the different folders to access recorded conversations, codes, and graphs.

## Folder Structure

- `RES`: Graphs folder for each group.
- `RESOURCES`: Folder containing recorded conversations from Wireshark.
- `src`: Directory containing all project codes and implementations.
- `Final project-computer networking.pdf`: Full project PDF document.
- `Final project-computer networking(Hebrew).pdf`: Hebrew version of the project PDF.

## References

- Article: [Practical Traffic Analysis Attacks on Secure Messaging Applications](link-to-article)
- LinkedIn: [Your LinkedIn Profile](link-to-your-LinkedIn)
- GitHub Repository: [Your GitHub Repository](https://github.com/vivianu2001/network_project)

