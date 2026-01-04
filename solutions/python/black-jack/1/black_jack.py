"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str, ace_eleven: bool = False):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        if ace_eleven:
            return 11
        return 1
    return int(card, base=10)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    first = value_of_card(card_one)
    second = value_of_card(card_two)
    if first == second:
        return (card_one, card_two)
    higher = max(first, second)
    if higher == first:
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    hand_value = value_of_card(card_one) + value_of_card(card_two)
    if hand_value + 11 > 21:
        return 1
    return 11


def hand_value(card_one, *args, ace_eleven: bool = False):
    value = value_of_card(card_one, ace_eleven)
    for card in args:
        value += value_of_card(card, ace_eleven)
    return value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    hv = hand_value(card_one, card_two, ace_eleven=True)
    return hv == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    va1 = value_of_card(card_one, ace_eleven=True)
    va2 = value_of_card(card_two, ace_eleven=True)
    return v1 == v2 or va1 == va2


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    hv = hand_value(card_one, card_two)
    return hv in [9, 10, 11]
