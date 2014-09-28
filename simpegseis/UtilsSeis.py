import numpy as np
import matplotlib.pyplot as plt

def clipsign (value, clip):
  clipthese = abs(value) > clip
  return value * ~clipthese + np.sign(value)*clip*clipthese

def wiggle (traces,skipt=1,scale=1.,lwidth=.1,offsets=None,redvel=0.,tshift=0.,sampr=1.,clip=10.,color='black',fill=True,line=True):

  ns = traces.shape[1]
  ntr = traces.shape[0]
  t = np.arange(ns)*sampr
  timereduce = lambda offsets, redvel, shift: [float(offset) / redvel + shift for offset in offsets]

  if (offsets is not None):
    shifts = timereduce(offsets, redvel, tshift)
  else:
    shifts = np.zeros((ntr,))

  for i in range(0, ntr, skipt):
    trace = traces[i].copy()
    trace[0] = 0
    trace[-1] = 0

    if (line):
      plt.plot(i + clipsign(trace / scale, clip), t - shifts[i], color=color, linewidth=lwidth)
    if (fill):
      for j in range(ns):
        if (trace[j] < 0):
          trace[j] = 0
      plt.fill(i + clipsign(trace / scale, clip), t - shifts[i], color=color, linewidth=0)
  plt.grid(True)
