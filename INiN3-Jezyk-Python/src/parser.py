#!/usr/bin/env python3

import re
import matplotlib.pyplot as plt
import numpy as np
import os

#from lagrange import lagrange
dir_path = os.path.dirname(os.path.realpath(__file__))

polynomial_degree = 3
# polynomial_degree = 5

with open(dir_path + '/data/log.log') as file:
    file_content = file.read().strip()
file.close()

p = re.compile(r'(\d+) E =(?:\s+)(.*) dE =(?:\s+)(\d.\d+[a-z]\+\d+) dH =(?:\s+)(\d.\d+[a-z]\+\d+)')
matches = p.findall(file_content)

x = []
E = []
dE = []
dH = []
for line in matches:
    x.insert(int(line[0]), int(line[0]))
    E.insert(int(line[0]), float(line[1]))
    dE.insert(int(line[0]), float(line[2]))
    dH.insert(int(line[0]), float(line[3]))


X, Y = np.meshgrid(x, E)
# lagrange()


fig = plt.figure()
fig.canvas.set_window_title('Wykres')

plt.plot(x, E, label='E')
plt.legend()

plt.plot(x, dE, label='dE')
plt.legend()

plt.plot(x, dH, label='dH')
plt.legend()

plt.show()
