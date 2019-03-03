import cv2
from midiutil import MIDIFile

THRESHHOLD = 5
DISTANCE = 100
DIST_BETWEEN_BARS = 20

def staffLines(_plines):
	plines = _plines.tolist()
	plines.sort(key=lambda x: x[0][1])
	min_x = 9999999
	max_x = -1
	lines = []
	temp = [0]
	dist = 0
	prevY = -THRESHHOLD - 1
	for coords in plines:
		if(abs(coords[0][0] - coords[0][2]) < 20):
			continue
		dist += abs(coords[0][0] - coords[0][2])
		if coords[0][0] < min_x:
			min_x = coords[0][0]
		if coords[0][2] > max_x:
			max_x = coords[0][2]
		if coords[0][1] > prevY + THRESHHOLD:
			if(dist > DISTANCE):
				avg = 0
				for line in temp:
					avg += line
				avg /= len(temp)
				lines.append(int(avg))
			temp = []
			dist = 0
			prevY = coords[0][1]
		temp.append(coords[0][1])
	if(dist > DISTANCE):
		avg = 0
		for line in temp:
			avg += line
		avg /= len(temp)
		lines.append(int(avg))
	lines.pop(0)
	i = 1
	while i < len(lines) - 1:
		if lines[i] - lines[i-1] > DIST_BETWEEN_BARS and lines[i+1] - lines[i] > DIST_BETWEEN_BARS:
			lines.pop(i)
		else:
			i+=1

	return lines, min_x, max_x

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