"""Funkcja która dokonuje przewidywania następnej wartości na podstawie danych otrzymanych na wejściu."""

from datetime import date
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np

arr = [20, -4, 201, -33, 100, 500, 123, -42, 120]


def predict_next_value(input_array):
    # Funkcja bierze na wejściu tablice dowolnej długości, w której znajdują się ZMIANY liczby
    # subskrypcji z dnia na dzień przez kilka dni, a następnie generuje predykcje jak będzie wyglądała ta liczba
    # następnego dnia (jutro). output[0] funkcji to powiększona o nową wartość tablica a output[1] to kolejne daty."""

    x = [i for i in range(len(input_array))]
    y = np.array(input_array)
    x = np.array(x)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]

    dates = [date.today() - timedelta(days=i) for i in range(-1, len(input_array))]
    dates_correct = [day.strftime('%d %b %Y').upper() for day in dates]
    dates_correct.reverse()

    input_array.append(int(m * len(y) + c))
    return input_array, dates_correct


output = predict_next_value(arr)
print(output[1], output[0])
