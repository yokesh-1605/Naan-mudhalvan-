import matplotlib.pyplot as plt

# Sample data: defects found in each of 10 batches
batches = list(range(1, 11))
defects_per_batch = [2, 1, 0, 3, 1, 0, 0, 2, 1, 1]

# First Pass Indicator: 1 if no defects, 0 otherwise
first_pass = [1 if defects == 0 else 0 for defects in defects_per_batch]

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for defects per batch
ax1.bar(batches, defects_per_batch, color='skyblue', label='Defects per Batch')
ax1.set_xlabel("Batch Number")
ax1.set_ylabel("Number of Defects", color='blue')
ax1.set_title("Phase 4 Quality Control Performance Metrics")
ax1.set_xticks(batches)

# Overlay First Pass Yield line
ax2 = ax1.twinx()
ax2.plot(batches, first_pass, 'go--', label='First Pass (1 = Pass)', linewidth=2)
ax2.set_ylabel("First Pass Indicator", color='green')

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
