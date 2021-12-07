import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
    position = []
    for line in lines[0].split(","):
        position.append(int(line))

    print(position)
    #position = [16,1,2,0,4,2,7,1,2,14]
    print(np.median(position))
    count = 0
    counta = 0

    #print(sum(1,5))
    length = max(position)
    print(max(position))
    tar = np.zeros(length)
    for target in range(length):
        #target = round(np.mean(position))
        steps = np.array(position) - target
        count = 0
        counta = 0
        #print(steps)
        #print(round(np.mean(position)))
        for step in steps:
            counta += abs(step)
            for i in range(abs(step)+1):
                count += i
        tar[target] = count
        print(target,count)
    print(min(tar))
