from collections import Counter

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'


def cross(A, B):
    """Cross product of elements in A and elements in B."""
    return [a + b for a in A for b in B]


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units
# So, modifying the assignment to resolve the diagonal sudoku puzzle
first_diagonal = [''.join(t) for t in zip(rows, cols)]  # top left to right bottom
unitlist.append(first_diagonal)
reversed_col = cols[::-1]
second_diagonal = [''.join(t) for t in zip(rows, reversed_col)]  # top right to left bottom
unitlist.append(second_diagonal)
# print(unitlist)


units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    for unit in unitlist:
        list_naked_twins = get_naked_twins(values, unit)
        # Eliminate the naked twins as possibilities for their peers
        values = eliminate_naked_twins(values, unit, list_naked_twins)
    return values


def eliminate_naked_twins(values, unit, list_naked_twins):
    """Eliminate the naked twins as possibilities for their peers.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        unit(list): a list of the form ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
        list_naked_twins(list): a list of tuples that contains naked twin values of the form [('A1', '23'), ('A7', '23')]

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Eliminate the naked twins as possibilities for their peers
    for naked_twin in list_naked_twins:
        for box in unit:
            if values[box] != naked_twin[1]:
                for digit in naked_twin[1]:
                    new_value = values[box] = values[box].replace(digit, '')
                    assign_value(values, box, new_value)
    return values


def get_naked_twins(values, unit):
    """
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the list of tuple as form of [('A1', '23'), ('A7', '23')]
    """
    tuples = [(box, values[box]) for box in unit if len(values[box]) == 2]
    return [x for x in tuples for y in tuples if (x != y and x[1] == y[1])]


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print


def eliminate(values):
    """ *
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')


# improved solution

def eliminate_naked_twins_improved(values, unit, list_naked_twins):
    """Eliminate the naked twins as possibilities for their peers.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        unit(list): a list of the form ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
        list_naked_twins(list): a list of tuples that contains naked twin values of the form [('A1', '23'), ('A7', '23')]

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Eliminate the naked twins as possibilities for their peers
    for naked_twin in list_naked_twins:
        for box in unit:
            if values[box] != naked_twin:
                for digit in naked_twin:
                    new_value = values[box] = values[box].replace(digit, '')
                    assign_value(values, box, new_value)
    return values


def get_naked_twins_improved(values, unit):
    """
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the list of tuple as form of [('A1', '23'), ('A7', '23')]
    """
    count_res = Counter(values[u] for u in unit)
    return [v for v, c in count_res.items() if len(v) == 2 and c == 2]  # IMPROVED HERE!
