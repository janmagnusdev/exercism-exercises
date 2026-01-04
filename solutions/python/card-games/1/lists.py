"""
Poker functions
"""


def get_rounds(number):
  """
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
  return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
  """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
  return rounds_1 + rounds_2


def list_contains_round(rounds, number):
  """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
  return number in rounds


def card_average(hand):
  """
  :param hand: list - cards in hand.
  :return:  float - average value of the cards in the hand.
  """

  length = len(hand)
  sum = 0
  for card in hand:
    sum += card
  return sum / length


def approx_average_is_average(hand):
  """
  :param hand: list - cards in hand.
  :return: bool - if approximate average equals to the `true average`.
  """
  avg = card_average(hand)
  first = hand[0]
  last = hand[-1]
  avg1 = (first + last) / 2
  avg2 = hand[len(hand) // 2]
  return avg == avg1 or avg == avg2


def average_even_is_average_odd(hand):
  """
  :param hand: list - cards in hand.
  :return: bool - are even and odd averages equal?
  """
  odd = [number for number in hand if number % 2 == 0]
  even = [number for number in hand if number % 2 == 1]
  odd_avg = card_average(odd)
  even_avg = card_average(even)
  return odd_avg == even_avg


def maybe_double_last(hand):
  """
  :param hand: list - cards in hand.
  :return: list - hand with Jacks (if present) value doubled.
  """
  maybe_jack = hand[-1] == 11
  if maybe_jack:
    return hand[:-1] + [22]
  return hand
