from mido import MidiFile, MidiTrack, Message
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


def apply_random_deviation(duration, deviation_range=40):
    deviation = random.randint(-deviation_range, deviation_range)
    return max(1, duration + deviation)


for _ in range(100):
    base_duration = random.choice([120, 60])

    duration = apply_random_deviation(base_duration)

    track.append(Message("note_on", note=60, velocity=64, time=0))
    track.append(Message("note_off", note=60, velocity=64, time=duration))

mid.save("random_rhythm_16th_32nd_notes.mid")
