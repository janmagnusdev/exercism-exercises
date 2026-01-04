SHARP = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

intervals_to_hs = {"m": 1, "M": 2, "A": 3}


def NOTE(pc: int, *, accidental="sharp") -> str:
    if accidental == "sharp":
        return SHARP[pc % 12]
    if accidental == "flat":
        return FLAT[pc % 12]
    raise ValueError("accidental must be 'sharp' or 'flat'")


class Scale:
    tonic = None

    def __init__(self, tonic):
        self.tonic = tonic
        pass

    def chromatic(self):
        # should return the chromatic scale
        intervals = "mmmmmmmmmmm"
        return self.interval(intervals)

    def get_tonic_index(self):
        # tonic casing is only relevant for determining sharp or flat accidentals
        uppercase_tonic = f"{self.tonic[:1].upper()}{self.tonic[1:]}"
        try:
            tonic_index = SHARP.index(uppercase_tonic)
        except ValueError:
            tonic_index = FLAT.index(uppercase_tonic)
        return tonic_index

    def interval(self, intervals: str):
        """
        :return: should return the scale made by applying the intervals
        """
        accidental = self.sharp_or_flat(self.tonic)
        tonic_index = self.get_tonic_index()

        scale_pcs = [tonic_index]
        intervals = list(intervals)
        for i, interval in enumerate(intervals):
            note = scale_pcs[i]
            scale_pcs.append(self.add_interval(note, interval))

        scale_notes = list(
            map(lambda note_idx: NOTE(note_idx, accidental=accidental), scale_pcs)
        )

        return scale_notes

    def add_interval(self, note_idx: int, interval: str) -> int:
        halfsteps = intervals_to_hs[interval]
        # pc = pitch class
        pc = (note_idx + halfsteps) % len(SHARP)
        return pc

    def sharp_or_flat(self, tonic: str):
        # hardcoded kinda sucks, there should be a dynamic way to calculate this, but oh well this is just an exercise
        # C is neutral accidentals, but default accidental is #
        sharp_tonics = ["C", "G", "D", "A", "E", "B", "F#"]
        sharp_minor_tonics = ["a", "e", "b", "f#", "c#", "g#", "d#"]
        flat_tonics = ["F", "Bb", "Eb", "Ab", "Db", "Gb"]
        flat_minor_tonics = ["d", "g", "c", "f", "bb", "eb"]

        return (
            "sharp"
            if (tonic in sharp_tonics or tonic in sharp_minor_tonics)
            else "flat"
        )