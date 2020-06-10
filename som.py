import random
import math


def euclidean_distance(a, b):
    size = len(a)
    result = 0

    for i in range(size):
        result += (a[i] - b[i]) ** 2

    return math.sqrt(result)


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y1)


def nearest_neuron(vector, weights, rows, columns):
    result = (0, 0)
    minimun_distance = 1.0e20

    for i in range(rows):
        for j in range(columns):
            distance = euclidean_distance(weights[i][j], vector)

            if distance < minimun_distance:
                minimun_distance = distance
                result = (i, j)

    return result


def adjust_weight(value, alpha, data):
    for i, val in enumerate(value):
        value[i] = value[i] + alpha * (data[i] - value[i])

    return value


def test_adjust_weight():
    value = [10, 10, 10]
    alpha = 0.5
    data = [2, 2, 2]
    print(adjust_weight(value, alpha, data))


def som(data):
    data_size = len(data)
    data_dimensions = len(data[0])

    # Inicializando variables
    rows = 5 # variable?
    cols = 5 # variable?
    dimensions = data_dimensions
    iterations = 1000 # variable?

    max_range = rows + cols
    learning_rate = 0.5 # variable?
    training_data = data

    # Creando las neuronas
    weights = [[[random.random() for _ in range(dimensions)]
                for _ in range(cols)] for _ in range(rows)]

    # Ejecutando algoritmo del SOM
    for it in range(iterations):
        alpha = 1.0 - it / iterations
        current_alpha = alpha * learning_rate
        current_range = int(alpha * max_range)

        t = random.randint(0, data_size - 1)

        (bmu_row, bmu_col) = nearest_neuron(data[t], weights, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if manhattan_distance(bmu_row, bmu_col, i, j) < current_range:
                    weights[i][j] = adjust_weight(weights[i][j], current_alpha, data[t])

    # retornar los datos?
    return weights
    # print(weights)
    # for row in weights:
    #     print(row)
