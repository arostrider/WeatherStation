# TODO: use numpy

import json

import matplotlib.pyplot as plt

with open(r'2022-05-29.json', 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)

subjects = ["temperature", "pressure", "humidity"]

x_axis = []
y_axis = {subj: [] for subj in subjects}

for timestamp, sample in data.items():
    x_axis.append(timestamp)

    for subj in subjects:
        y_axis[subj].append(sample[subj])

for subj in subjects:
    plt.grid(True)
    plt.plot(x_axis, y_axis[subj], color='maroon')
    plt.xlabel('time')
    plt.ylabel(subj)
    plt.xticks(range(0, len(x_axis), 100))
    plt.show()
