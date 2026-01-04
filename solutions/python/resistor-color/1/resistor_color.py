COLORS = [
    color.lower()
    for color in ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]
]


def color_code(color):
  return COLORS.index(color)


def colors():
  return COLORS
