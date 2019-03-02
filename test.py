import cv2
from midiutil import MIDIFile

THRESHHOLD = 3

def staffLines(plines):
	plines = sorted(plines, key=lambda x: x[0])
	lines = []
	temp = [0]
	prevY = -THRESHHOLD - 1
	for coords in plines:
		if coords[0] > prevY + THRESHHOLD:
			avg = reduce(lambda x, y: x + y, temp), len(temp)
			lines.append(avg)
			temp = []
			prevY = coords[0]
		temp.append(coords[0])
	avg = reduce(lambda x, y: x + y, temp), len(temp)
	lines.append(avg)
	lines.pop(0)
	return lines

def writeMIDI(fileName, notes):
	
	track    = 0
	channel  = 0
	time     = 0    # In beats
	duration = 1    # In beats
	tempo    = 60   # In BPM
	volume   = 100  # 0-127, as per the MIDI standard
	
	MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
						# automatically)
	MyMIDI.addTempo(track, time, tempo)
	
	# adds each note to the track
	for note in notes:
		MyMIDI.addNote(track, channel, pitch, time, note[0], volume)
		time += note[1]
	
	# writes to the filename
	with open(fileName, "wb") as output_file:
		MyMIDI.writeFile(output_file)