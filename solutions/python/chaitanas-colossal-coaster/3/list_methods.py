"""
Docstring
"""
EXPRESS_Q = 1
NORMAL_Q = 0


def add_me_to_the_queue(express_queue: list, normal_queue, ticket_type, person_name):
    """
    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type not in [EXPRESS_Q, NORMAL_Q]:
        raise ValueError("invalid ticket type")
    if ticket_type == EXPRESS_Q:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == NORMAL_Q:
        normal_queue.append(person_name)
        return normal_queue
    return []


def find_my_friend(queue, friend_name):
    """
    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    for i, value in enumerate(queue):
        if value == friend_name:
            return i
    return -1


def add_me_with_my_friends(queue, index, person_name):
    """
    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """
    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    queue.pop(queue.index(person_name))
    return queue


def how_many_namefellows(queue, person_name):
    """
    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    count = 0
    for i in range(len(queue)):
        if queue[i] == person_name:
            count += 1
    return count


def remove_the_last_person(queue):
    """
    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue):
    """
    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    return sorted(queue)
