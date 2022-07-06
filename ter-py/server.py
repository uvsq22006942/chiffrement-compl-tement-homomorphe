import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

from util import text2array
fh = open('cA', 'r')
ca = text2array(fh.read())
fh.close()

print('Loaded [ca] from cA')

fh = open('cB', 'r')
cb = text2array(fh.read())
fh.close()

print('Loaded [cb] from cB')

def write2file(c):
    fh = open('fAB', 'w')
    print(c, file=fh)
    fh.close()
    print('Wrote matrix to fAB')

c = ca + cb * 1
write2file(c)

# [demoClient.py]
# [python -i demoServer.py]