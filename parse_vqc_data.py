from pennylane import numpy as np

def concatenated_string_to_array(string):
    """DO NOT MODIFY THIS FUNCTION.
    Turns a concatenated string of integers separated by commas into
    an array of integers. (Inverse of array_to_concatenated_string).
    """
    return np.array([int(x) for x in string.split(",")])


def parse_input():
    """DO NOT MODIFY THIS FUNCTION.
    Parse the input data into 3 arrays: the training data, training labels,
    and testing data.
    Dimensions of the input data are:
      - X_train: (250, 3)
      - Y_train: (250,)
      - X_test:  (50, 3)
    """
    with open("1.in", "r") as infile:
        giant_string = infile.readline()

    X_train_part, Y_train_part, X_test_part = giant_string.split("XXX")

    X_train_row_strings = X_train_part.split("S")
    X_train_rows = [[float(x) for x in row.split(",")] for row in X_train_row_strings]
    X_train = np.array(X_train_rows)

    Y_train = concatenated_string_to_array(Y_train_part)

    X_test_row_strings = X_test_part.split("S")
    X_test_rows = [[float(x) for x in row.split(",")] for row in X_test_row_strings]
    X_test = np.array(X_test_rows)

    with open("1.ans", "r") as infile:
        test_string = infile.readline()
    Y_test = concatenated_string_to_array(test_string)
    
    X_train.requires_grad = False
    X_test.requires_grad = False
    Y_train.requires_grad = False
    Y_test.requires_grad = False
    
    return X_train, Y_train, X_test, Y_test