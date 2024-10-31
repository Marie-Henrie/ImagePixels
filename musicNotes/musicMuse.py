from music21 import stream, note, interval

# Define your tone table as a list of lists (rows of tones)
tone_table = [
    ['B1', 'B1', 'B2', 'B2', 'A#', 'B2', 'B2', 'B1', 'C#1'],
    ['C#1', 'D#3', 'B1', 'B2', 'B2', 'B1', 'B1', 'F#1', 'C#2'],
    ['C#1', 'D1', 'D1', 'B1', 'B1', 'B1', 'G#3', 'G#3', 'C#2'],
    ['C#1', 'D1', 'D1', 'C#1', 'C#1', 'G#3', 'G#3', 'C#2', 'C#2'],
    ['C#2', 'B1', 'B1', 'D1', 'D1', 'B2', 'B2', 'C#2', 'D1'],
    ['B2', 'B2', 'C3', 'C#1', 'B1', 'B2', 'C3', 'C#2', 'C#1'],
    ['B2', 'B1', 'C#1', 'C#1', 'F#1', 'G#3', 'B1', 'C#1', 'C#1'],
    ['B2', 'B1', 'C#1', 'F#2', 'D#3', 'G#3', 'B1', 'C#1', 'C#1'],
    ['G#3', 'B1', 'C#1', 'F#2', 'F#2', 'G#3', 'B1', 'C#1', 'C#1']
]

# Define a function to interpret notes with specific octave rules
def parse_tone(tone_str):
    if '/' in tone_str:  # Handle cases like 'H/B1' which are equivalent to 'B1'
        tone_str = tone_str.split('/')[-1]
    
    pitch_name = tone_str[:-1] if tone_str[-1].isdigit() else tone_str  # Pitch
    octave_modifier = int(tone_str[-1]) if tone_str[-1].isdigit() else None

    # Map "H" notation to "B" to comply with standard notation
    if pitch_name == 'H':
        pitch_name = 'B'

    # Set octave based on rules: None -> octave 3, 1 -> octave 4, etc.
    octave = 3 + (octave_modifier if octave_modifier is not None else 0)
    return f"{pitch_name}{octave}"

# Create a music21 stream to hold the notes
score = stream.Score()

# Add each row of the tone table as a new measure (line in the song)
for row in tone_table:
    measure = stream.Measure()
    previous_note_name = None
    duplicate_count = 0
    row_length = len(row)

    for idx, tone in enumerate(row):
        note_name = parse_tone(tone)
        n = note.Note(note_name)
        
        # Check if the current note is the same as the previous one
        if note_name == previous_note_name:
            duplicate_count += 1
        else:
            duplicate_count = 1  # Reset count on new note

        # Apply rules based on the duplicate count
        if duplicate_count == 2:
            # Two consecutive identical notes become eighth notes
            n.quarterLength = 0.5
        elif duplicate_count == 3:
            # Three consecutive identical notes become two eighth notes and go up
            # First note transposed up by a whole step
            transposed_note = n.transpose(interval.Interval('M2'))
            transposed_note.quarterLength = 0.5  # First note as an eighth note
            measure.append(transposed_note)
            # Add second note as the next note in the sequence
            n.quarterLength = 0.5  # Second note as an eighth note
        elif duplicate_count >= 4:
            # For every four or more identical notes, set to sixteenth notes
            n.quarterLength = 0.25
            if duplicate_count % 2 == 0:  # If it's the second of a pair of 16th notes
                n = n.transpose(interval.Interval('M2'))  # Transpose it up by a whole step
        else:
            n.quarterLength = 1  # Default to a quarter note for non-duplicates

        # Add note to measure and set as previous note
        measure.append(n)
        previous_note_name = note_name

    score.append(measure)

# Set the last note in the entire score to a half note if it differs from the previous one
if score.flat.notes:
    last_note = score.flat.notes[-1]
    second_last_note = score.flat.notes[-2] if len(score.flat.notes) > 1 else None
    if second_last_note and last_note.nameWithOctave != second_last_note.nameWithOctave:
        last_note.quarterLength = 2  # Set the last note to a half note

# Show the score or save it as a MIDI/PNG/PDF
# Uncomment the line below to show the score using MuseScore or your default music editor.
# score.show()

# Export as MusicXML and MIDI for notation programs or playback
score.write("musicxml", fp="tone_table_song.xml")
score.write("midi", fp="tone_table_song.mid")

score.show()









'''
from music21 import stream, note, interval

# Define your tone table as a list of lists (rows of tones)
tone_table = [
    ['G#3', 'B1', 'B1', 'B1', 'B2', 'B2', 'B2', 'B2', 'B2', 'B2', 'B2', 'B2'],
    ['G#3', 'B1', 'C#1', 'B1', 'B2', 'B2', 'B2', 'B2', 'B2', 'F#1', 'B1', 'B2'],
    ['G3', 'B1', 'B1', 'B1', 'B1', 'B2', 'B1', 'B2', 'B1', 'B1', 'B1', 'B2'],
    ['B1', 'B1', 'B1', 'B1', 'B1', 'C#1'],
    ['B1', 'B1', 'G3', 'G#1', 'D#2', 'F2', 'F1', 'B1', 'B1', 'B1', 'C1', 'D#1'],
    ['G3', 'G3', 'G3', 'C#1', 'C#1', 'D#1', 'D#1', 'F3', 'C#1', 'C#1', 'C1', 'D#1'],
    ['G3', 'G3', 'B1', 'C#1', 'D#1', 'D#1', 'D#2', 'F3', 'C#1', 'B1', 'C1', 'C1'],
    ['G3', 'G#2', 'G#1', 'D#1', 'D#1', 'C#1', 'C#1', 'C#1', 'C#2', 'C#1', 'B1', 'A#1']
]

# Define a function to interpret notes with specific octave rules
def parse_tone(tone_str):
    if '/' in tone_str:  # Handle cases like 'H/B1' which are equivalent to 'B1'
        tone_str = tone_str.split('/')[-1]
    
    pitch_name = tone_str[:-1] if tone_str[-1].isdigit() else tone_str  # Pitch
    octave_modifier = int(tone_str[-1]) if tone_str[-1].isdigit() else None

    # Map "H" notation to "B" to comply with standard notation
    if pitch_name == 'H':
        pitch_name = 'B'

    # Set octave based on rules: None -> octave 3, 1 -> octave 4, etc.
    octave = 3 + (octave_modifier if octave_modifier is not None else 0)
    return f"{pitch_name}{octave}"

# Create a music21 stream to hold the notes
score = stream.Score()

# Add each row of the tone table as a new measure (line in the song)
for row in tone_table:
    measure = stream.Measure()
    previous_note_name = None
    duplicate_count = 0

    for idx, tone in enumerate(row):
        note_name = parse_tone(tone)
        n = note.Note(note_name)
        
        # Check if the current note is the same as the previous one
        if note_name == previous_note_name:
            duplicate_count += 1
        else:
            duplicate_count = 1  # Reset count on new note

        # Apply rules based on the duplicate count
        if duplicate_count == 2:
            # Two consecutive identical notes become eighth notes
            n.quarterLength = 0.5
        elif duplicate_count == 3:
            # Three consecutive identical notes become two eighth notes and go up
            # First note transposed up by a whole step
            transposed_note = n.transpose(interval.Interval('M2'))
            transposed_note.quarterLength = 0.5  # First note as an eighth note
            measure.append(transposed_note)
            # Add second note as the next note in the sequence
            n.quarterLength = 0.5  # Second note as an eighth note
        elif duplicate_count >= 4:
            # For every four or more identical notes, set to sixteenth notes
            n.quarterLength = 0.25
            if duplicate_count % 2 == 0:  # If it's the second of a pair of 16th notes
                n = n.transpose(interval.Interval('M2'))  # Transpose it up by a whole step
        else:
            n.quarterLength = 1  # Default to a quarter note for non-duplicates

        # Add note to measure and set as previous note
        measure.append(n)
        previous_note_name = note_name
    
    score.append(measure)

# Show the score or save it as a MIDI/PNG/PDF
# Uncomment the line below to show the score using MuseScore or your default music editor.
# score.show()

# Export as MusicXML and MIDI for notation programs or playback
score.write("musicxml", fp="tone_table_song.xml")
score.write("midi", fp="tone_table_song.mid")

score.show()
'''