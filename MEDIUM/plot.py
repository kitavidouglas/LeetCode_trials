import matplotlib.pyplot as plt

# Define the event times and corresponding queue lengths
times = [0.0, 1.4, 2.0, 2.4, 3.1, 3.2, 4.0, 5.2, 5.8, 7.2, 8.3, 8.9, 9.6]
queue_lengths = [0, 1, 2, 1, 0, 0, 1, 0, 1, 2, 3, 4, 3]

# Create step plot
plt.figure(figsize=(12, 6))
plt.step(times, queue_lengths, where='post', label="Queue Length", color='blue')
plt.fill_between(times, queue_lengths, step='post', alpha=0.2)

# Labels and title
plt.title("Time Path of Queue Length in Single-Server Queue", fontsize=14)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Queue Length", fontsize=12)
plt.grid(True)
plt.xticks(times)
plt.legend()
plt.tight_layout()
plt.show()
