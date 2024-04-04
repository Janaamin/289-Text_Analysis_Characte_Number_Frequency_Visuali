import matplotlib.pyplot as plt
import collections

# Read the file
with open('syllabus.txt', 'r') as file:
    text = file.read().lower()  # Convert to lowercase

# Count occurrences of letters and numbers
char_counts = collections.Counter(char for char in text if char.isalnum())

# Sort the counts
sorted_counts = dict(sorted(char_counts.items()))

# Extract data for plotting
characters = list(sorted_counts.keys())
counts = list(sorted_counts.values())

#the bar chart
plt.figure(figsize=(15, 5))
plt.bar(characters, counts, color='red', width=.9)

# Add chart title and labels
plt.title('Letter and Number Occurrences in Syllabus', fontsize=16, color="black")
plt.xlabel('Letters and Numbers', fontsize=16)
plt.ylabel('Counts', fontsize=16)

# Add value labels on top of bars
for i, count in enumerate(counts):
    plt.text(i - 0.50, count + 0.50, str(count), color='black', fontweight='bold')

# Show the plot
plt.show()