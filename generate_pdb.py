from mido import MidiFile, MidiTrack, Message
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("Calcitriol", "HMDB0001903 (Calcitriol)_3D.pdb")

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                x, y, z = atom.get_coord()

                note = int((x % 1) * 127)
                note = max(0, min(note + 60, 127))

                velocity = int((y % 1) * 127)
                velocity = max(0, min(velocity, 127))

                duration = int((z % 1) * 480) + 60

                track.append(Message("note_on", note=note, velocity=velocity, time=0))
                track.append(
                    Message("note_off", note=note, velocity=velocity, time=duration)
                )

mid.save("Calcitriol.mid")
