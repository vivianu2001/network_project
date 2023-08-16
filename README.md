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

The project is based on the "Practical Traffic Analysis Attacks on Secure Messaging Applications" article, focusing on answering project questions through the analysis of 7 WhatsApp groups. The analysis involves the recording of WhatsApp conversations using Wireshark and the implementation of the event based detector algorithm detailed in the article.

## Methodology

1. Recorded WhatsApp Conversations: The conversations were captured using Wireshark to obtain network traffic data.
2. Implemented event_extraction.py: Using the event based detector algorithm, the event_extraction.py script was created. It produces graphs that reveal the size and nature of messages within each WhatsApp group based on network packet information.
3. PDF and CCDF Graphs: Mathematical graphs were generated using `whatsapp_chat_histogram.py` for PDF functions and `message_size_distribution_ccdf.py` for CCDF functions. These tools allowed insights into message distribution patterns.

## Results
- Graphs for Message Sizes: The produced graphs under the `res` folder for each group (named `group_x_ee`) display the size of messages in each WhatsApp group based on network packet analysis.
- Message Over Time: `messeges_over_time` in the `res` folder for each group (named `group_x_mot`) illustrating package sizes over the duration of each group.
- PDF and CCDF Functions: `histogram_group_x` folder contains PDF graphs for groups with substantial message counts (groups 6 and 7), while CCDF graphs are produced using `message_size_distribution_ccdf.py`.
  
In our analysis, we investigated the network traffic from WhatsApp messages in different groups. We made interesting observations and faced several challenges in deciphering the data.
It can be concluded that the algorithms in the article do demonstrate the potential to discern group communication patterns Although challenges exist, this analysis provides important insights into the nature of different groups and can be a valuable tool for understanding the dynamics of WhatsApp groups.
As for the question of whether it is possible to understand whether it is possible to identify the groups in which the attacked participates when he communicates with several groups at the same time, it can be seen that this is relatively very complex. Even if the attacker participates in groups we participate in. There will be a very large "mixing" of messages, and it is not possible to analyze which group each package belongs to. When the attacker listens to a single group, it is relatively easy to export the events and analyze them according to the nature of the messages and the sending times.
 WhatsApp Web uses protocols in different data formats to facilitate communication between the client and the server.
When we checked the groups, we tried to do it during "quiet" times in order to get as clean a recording as possible and to be sure that these are indeed the packages related to the only WhatsApp groups in which we are active for a limited time. (whether we send messages or receive messages). When messages are sent simultaneously from several calls, the matter is more complex and it will not be possible to accurately identify which packages are related to which call.
More than that, we noticed that the attacker must also calculate and create a graph as real as possible with an appropriate threshold in order to get the nature of the events in the group. In addition, he must clean the packages that are bothering him.
That's why we think that in the end it takes time and investment and the attacker should be in the group in order not to "get lost" in all the information that passes through the attacked network.
When the attacker tries to coordinate a person's presence in multiple groups or channels, they face several challenges due to the nature of the WhatsApp application we studied. why?
1. End-to-end encryption: when the messages are encrypted, they can only be deciphered on the device of the recipient of the message. This means that even if the adversary can intercept the encrypted messages, he cannot read the content without the encryption keys. This encryption makes it difficult for the attacker to directly access the content of the messages, and understand which messages are related to which group.
2. Mixing messages: Messages from different groups or conversations are often mixed in the network traffic. This mixing challenges the attacker to distinguish between messages belonging to different groups. They can observe the traffic flow and the size of the messages, but without access to the encryption keys, it is not possible to determine the exact content or which messages belong to which group.
3. Packet size and timing: While the content of messages is encrypted, certain metadata such as message timing, size and frequency of communication are still visible to an attacker. However, as we have seen in the work, metadata alone may not be sufficient to reliably correlate an individual's presence in multiple groups. For example, multiple groups may have similar movement patterns, which becomes a challenge.
4. Multiple identities: frequent users, use several platforms when they enter the application, such as from the computer/phone.
This means that even if the attacker watches multiple interactions from different devices, he cannot definitively link them to the same person.
Furthermore, users may switch between devices or change their identity, further complicating the process.


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
- 'project-Instruction.pdf':Instruction and questions given to us.
- `res`: Graphs folder for each group.
- `resources`: Folder containing recorded conversations from Wireshark.
- `src`: Directory containing all project codes and implementations.
- `Final project-computer networking.pdf`: Full project PDF document.
- `Final project-computer networking-heb.pdf`: Hebrew version of the project PDF and the dry part.

## References

- Article: [Practical Traffic Analysis Attacks on Secure Messaging Applications](https://www.ndss-symposium.org/wp-content/uploads/2020/02/24347-paper.pdf)
- LinkedIn: www.linkedin.com/in/vivian-umansky-86b9a0288,
            https://www.linkedin.com/in/liraz-balas-274044249 
- GitHub Repository:https://github.com/vivianu2001/network_project

