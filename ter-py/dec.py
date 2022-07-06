from util import *
from enc import buildGadget
import numpy as np
from scipy.stats import mode


def decrypt(keys, ciphertext):
    stat("Decrypting message")
    msg = np.dot(keys.SK, ciphertext) % keys.q
    g = buildGadget(keys.l, keys.n)
    sg = np.dot(keys.SK, g) % keys.q
    div = np.rint((msg / sg).astype(np.float)).astype(np.int64)
    modes = np.unique(div, return_counts=True)
    modes = sorted(zip(modes[0], modes[1]), key=lambda t: -t[1])
    best_num = 0
    best_dist = float('inf')
    for mu, count in modes:
        dist = (msg - mu*sg) % keys.q
        dist = np.minimum(dist, keys.q - dist)
        # dist = np.linalg.norm(dist)
        dist = np.dot(dist, dist)
        if dist < best_dist:
            best_num = mu
            best_dist = dist
    return best_num
