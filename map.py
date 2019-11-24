import numpy as np
from random import randint
SIZE = 7

class map:
    def __init__(self):
        self.tab_map = []
        room_start, room_end = self.initmap()
        print(self.tab_map)
        print("Start room : ", room_start, ", ", "End room", room_end)
        #  print("Map from __init__ : ", self.tab_map)

    def initmap(self):
        n = SIZE
        x = np.zeros(n)
        y = np.zeros(n)
        for i in range(1, n):
            val = randint(1, 4)
            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1

        for i in range(SIZE):
            self.tab_map.append(((x[i], y[i]), 1))

        room_start = self.tab_map[0]
        room_end = self.tab_map[SIZE-1]
        return room_start, room_end

map = map()
