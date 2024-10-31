import matplotlib.pyplot as plt

# Sample tone table
tone_table = [
    ['G#3', 'H/B1', 'H/B1', 'H/B1', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'H/B2'],
    ['G#3', 'H/B1', 'C#1', 'H/B1', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'H/B2', 'F#1', 'H/B1', 'H/B2'],
    ['G3', 'H/B1', 'H/B1', 'H/B1', 'H/B1', 'H/B2', 'H/B1', 'H/B2', 'H/B1', 'H/B1', 'H/B1', 'H/B2'],
    # Add more rows as needed
]

# Mapping of notes to y-axis positions (for simplicity, this is arbitrary)
note_positions = {
    'G#3': 3, 'H/B1': 1, 'H/B2': 2, 'C#1': 4, 'C#2': 5,
    'G3': 6, 'G#1': 7, 'G#2': 8, 'B1': 9, 'D#1': 10,
    'D#2': 11, 'F1': 12, 'F2': 13, 'F3': 14, 'A#1': 15
}

# Plot each line as a separate row
plt.figure(figsize=(12, 6))
for i, row in enumerate(tone_table):
    x = list(range(len(row)))  # Position each note along the x-axis
    y = [note_positions.get(note, 0) for note in row]  # Map each note to a y-axis position
    plt.plot(x, [i * 2 + pos for pos in y], marker='o', label=f'Line {i+1}')  # Offset by row

# Formatting the plot
plt.yticks(range(0, len(note_positions) * 2, 2), list(note_positions.keys()))
plt.xlabel("Time (Beats)")
plt.ylabel("Pitch")
plt.title("Simple Representation of Song Notes")
plt.legend()
plt.grid()
plt.show()
