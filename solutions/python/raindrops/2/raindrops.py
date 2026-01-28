def convert(number):
    drops = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }
    sounds = []

    for factor, sound in drops.items():
        if number % factor == 0:
            sounds.append(sound)

    return str(number) if len(sounds) == 0 else "".join(sounds)
