from music21 import stream, note, clef, meter, chord

# Create a Score to hold the piano part
score = stream.Score()

# Create two Parts for left and right hand
right_hand = stream.Part()
left_hand = stream.Part()

# Set the time signature (optional)
time_signature = meter.TimeSignature('4/4')
right_hand.append(time_signature)
left_hand.append(time_signature)

# Assign clefs to each hand
right_hand.append(clef.TrebleClef())
left_hand.append(clef.BassClef())

# Add some notes to the right hand (treble)
right_hand.append(note.Note('C5', quarterLength=1))
right_hand.append(note.Note('E5', quarterLength=1))
right_hand.append(note.Rest(quarterLength=1))  # Rest for rhythm
right_hand.append(note.Note('G5', quarterLength=1))

# Add some notes to the left hand (bass)
left_hand.append(note.Note('C3', quarterLength=1))
left_hand.append(note.Rest(quarterLength=1))
left_hand.append(chord.Chord(['E3', 'G3'], quarterLength=2))  # Adding a chord

# Combine left and right hands into the score
score.append(right_hand)
score.append(left_hand)

# Show or save the score as needed
score.show()  # This will display the score in MuseScore or the default editor
# Uncomment to export to MusicXML or MIDI format
# score.write("musicxml", fp="piano_score.xml")
# score.write("midi", fp="piano_score.mid")





'''from music21 import stream, note, clef, meter, chord

# Create a Score to hold the piano part
score = stream.Score()

# Create two Parts for left and right hand
right_hand = stream.Part()
left_hand = stream.Part()

# Set the time signature (optional)
time_signature = meter.TimeSignature('4/4')
right_hand.append(time_signature)
left_hand.append(time_signature)

# Assign clefs to each hand
right_hand.append(clef.TrebleClef())
left_hand.append(clef.BassClef())

# Add some notes to the right hand (treble)
right_hand.append(note.Note('C5', quarterLength=1))
right_hand.append(note.Note('E5', quarterLength=1))
right_hand.append(note.Rest(quarterLength=1))  # Rest for rhythm
right_hand.append(note.Note('G5', quarterLength=1))

# Add some notes to the left hand (bass)
left_hand.append(note.Note('C3', quarterLength=1))
left_hand.append(note.Rest(quarterLength=1))
left_hand.append(chord.Chord(['E3', 'G3'], quarterLength=2))  # Adding a chord

# Combine left and right hands into the score
score.append(right_hand)
score.append(left_hand)

# Show or save the score as needed
score.show()  # This will display the score in MuseScore or the default editor
# Uncomment to export to MusicXML or MIDI format
# score.write("musicxml", fp="piano_score.xml")
# score.write("midi", fp="piano_score.mid")
'''