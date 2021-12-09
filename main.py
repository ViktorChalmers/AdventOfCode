import numpy as np
def getVonNeumannNeighbors(state,index):
    expandedState = np.pad(state, 1, 'linear_ramp', end_values=(10, 10))
    #print(expandedState)
    index = index+1

    self = expandedState[index[0],index[1]]
    up = expandedState[index[0]-1,index[1]]
    down = expandedState[index[0]+1,index[1]]
    left = expandedState[index[0],index[1]-1]
    right = expandedState[index[0],index[1]+1]
    list = np.array([int(up), int(down), int(left), int(right)])

    return [int(self), list]

with open("input.txt") as f:
    lines = f.readlines()
    state = np.zeros([len(lines),len(lines[0])-1])
    #print(lines)
    for i in range(len(lines)):
        line = lines[i].replace("\n","")
        for j in range(len(line)):
            state[i,j] = int(line[j])

print(state)
heightMap = 0
for i in range(len(state)):
    for j in range(len(state[0])):
        [self, list] = getVonNeumannNeighbors(state,np.array([i,j]))
        if all(x>self for x in list):
            heightMap += self+1
print(heightMap)