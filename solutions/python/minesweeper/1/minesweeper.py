def annotate(minefield):
    # Function body starts here
    valid(minefield)

    annotated_minefield = minefield.copy()
    # convert strings in annotated minefield into char lists, making it easier to assign chars to an index pair
    for i, row_string in enumerate(annotated_minefield):
        annotated_minefield[i] = list(row_string)
        
    for row_i, row in enumerate(minefield):
        for column_j, char in enumerate(row):
            if char == "*":
                continue
            
            # create list of indexes that are neighbors
            # then check the list: throw out all invalid indexes after creating the list
            neighbors_to_check = [
                                (row_i - 1, column_j - 1), 
                                (row_i - 1, column_j),
                                (row_i - 1, column_j + 1),
                                (row_i, column_j - 1),
                                (row_i, column_j),
                                (row_i, column_j + 1),
                                (row_i + 1, column_j - 1),
                                (row_i + 1, column_j),
                                (row_i + 1, column_j + 1)
            ]
            min_index = 0
            # max_index_j is the same across all rows, since that is a precondition: all rows must have the same length
            max_index_i = len(minefield) - 1
            max_index_j = len(minefield[0]) - 1
            neighbors_to_check = filter(lambda x: min_index <= x[0] <= max_index_i and min_index <= x[1] <= max_index_j, neighbors_to_check)
            count = 0
            for neighbor in neighbors_to_check:
                i = neighbor[0]
                j = neighbor[1]
                if minefield[i][j] == "*":
                    count += 1
            if count == 0:
                annotated_minefield[row_i][column_j] = " "
            else:
                annotated_minefield[row_i][column_j] = str(count)

    # convert char lists back to strings
    for i, row in enumerate(annotated_minefield):
        annotated_minefield[i] = "".join(row)
    return annotated_minefield

def valid(minefield):
    valid = True
    # all rows must have the same length
    for row in minefield:
        if len(row) != len(minefield[0]):
            raise ValueError("The board is invalid with current input.")
    # valid chars must be used
    valid_chars = ["*", " "]
    for row in minefield:
        for symbol in row:
            if symbol not in valid_chars:
                raise ValueError("The board is invalid with current input.")
        