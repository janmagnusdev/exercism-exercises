EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers: int) -> int:
    """
    Return total preparation time in minutes for given count of layers.

    Input:
    layers - amount of layers
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """
    This is an awesome doc string for this stupid function
    """
    return (layers * PREPARATION_TIME) + elapsed_bake_time