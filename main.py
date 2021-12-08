import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
    position = []
    for line in lines[0].split(","):
        position.append(int(line))

    count = 0
    target = int(np.median(position))
    steps = np.array(position) - target
    count += sum(abs(steps))
    print(f"target = {target}, fuel consumption = {count}")

    count = 0
    target = (round(np.mean(position))-1)
    steps = np.array(position) - target
    count = 0
    print(target)
    for step in steps:
        #count += (step**2+step)/2
        for i in range(abs(step)+1):
            count += i
    print(f"target = {target}, fuel consumption = {count}")