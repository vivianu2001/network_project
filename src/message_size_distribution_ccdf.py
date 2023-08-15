import numpy as np
import matplotlib.pyplot as plt
import pyshark


# Read packet sizes from a pcapng file for a specific group
def read_group_data(file_path):
    cap = pyshark.FileCapture(file_path)
    sizes = [int(packet.length) for packet in cap]
    cap.close()
    return sizes


group1_sizes = read_group_data('/home/vivian/pdf_mess.pcapng')
group2_sizes = read_group_data('/home/vivian/audio_mess.pcapng')
group3_sizes = read_group_data('/home/vivian/video_m(group 2)_new.pcapng')
group4_sizes = read_group_data('/home/vivian/group_5.pcapng')
group5_sizes = read_group_data('/home/vivian/group_1.pcapng')



# Normalize packet sizes to their maximum
def normalize_sizes(sizes):
    max_size = max(sizes)
    normalized_sizes = np.array(sizes) / max_size
    return normalized_sizes


group1_sizes_normalized = normalize_sizes(group1_sizes)
group2_sizes_normalized = normalize_sizes(group2_sizes)
group3_sizes_normalized = normalize_sizes(group3_sizes)
group4_sizes_normalized = normalize_sizes(group4_sizes)
group5_sizes_normalized = normalize_sizes(group5_sizes)

# Sort the normalized sizes in descending order
group1_sizes_normalized = np.sort(group1_sizes_normalized)[::-1]
group2_sizes_normalized = np.sort(group2_sizes_normalized)[::-1]
group3_sizes_normalized = np.sort(group3_sizes_normalized)[::-1]
group4_sizes_normalized = np.sort(group4_sizes_normalized)[::-1]
group5_sizes_normalized = np.sort(group5_sizes_normalized)[::-1]


# Calculate CCDF values
def calculate_ccdf(normalized_sizes):
    ccdf = 1 - np.arange(1, len(normalized_sizes) + 1) / len(normalized_sizes)
    return ccdf


ccdf_group1 = calculate_ccdf(group1_sizes_normalized)
ccdf_group2 = calculate_ccdf(group2_sizes_normalized)
ccdf_group3 = calculate_ccdf(group3_sizes_normalized)
ccdf_group4 = calculate_ccdf(group4_sizes_normalized)
ccdf_group5 = calculate_ccdf(group5_sizes_normalized)

# Plot 1 - CCDF
plt.plot(group1_sizes_normalized, 1 - ccdf_group1, label='File messages', marker='o')
plt.plot(group2_sizes_normalized, 1 - ccdf_group2, label='Voice messages', marker='s')
plt.plot(group3_sizes_normalized, 1 - ccdf_group3, label='Video messages', marker='^')
plt.plot(group4_sizes_normalized, 1 - ccdf_group4, label='Text messages', marker='x')
plt.plot(group5_sizes_normalized, 1 - ccdf_group5, label='Image messages', marker='D')


plt.xlabel('Normalized Packet Size')
plt.ylabel('1 - Complementary CDF')
plt.title('Complementary CDF of Packet Size for Different Groups')
plt.legend()
plt.grid(True)
plt.show()
