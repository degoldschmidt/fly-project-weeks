import numpy as np
import matplotlib.pyplot as plt  ## package for plotting
import seaborn as sns
import prettyplotlib as pplt  ## package for plotting
from pylab import *
from matplotlib import rc
plt.rc('font', family='sans-serif')
plt.rc('text', usetex=True)
plt.rcParams['font.sans-serif'] = 'Futura'
plt.rcParams['font.serif'] = 'Futura'
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rc('mathtext', fontset='stixsans')
plt.close('all')

mydt = np.dtype([ ('name', np.str_, 16), 
                 ('id', np.str_, 1), 
                 ('x', np.int),
                 ('y', np.int),
                 ('size', np.int),
                 ('secsize', np.int) ] )
data = np.loadtxt("../data/fly1.csv", skiprows=1)   
params = np.genfromtxt('../data/processed/arena.cfg', skip_header=1, delimiter=' ', dtype=mydt)


### Setup arena dimensions
fac = 45./params['size']

def toSI(x, off):
    return fac*(x-off)
x0 = toSI(params['x']-params['size'], params['x'])
x1 = toSI(params['x']+params['size'], params['x'])
y0 = toSI(params['y']-params['size'], params['y'])
y1 = toSI(params['y']+params['size'], params['y'])
arena=plt.Circle( (toSI(params['x'],params['x']), toSI(params['y'],params['y']) ), toSI(params['size'],0),color='g',fill=False)


fig = figure(figsize=(8.8,8.4))
axes = plt.gca()
plt.xlim([x0+(x0/10),x1+(x1/10)])
plt.ylim([y0+(y0/10),y1+(y1/10)])
lbfs = 16
plt.xlabel('x [mm]', fontsize=lbfs)
plt.ylabel('y [mm]', rotation='horizontal', fontsize=lbfs)
pplt.plot(toSI(data[:,1],params['x']), toSI(data[:,2],params['y']), 'k.', markersize=2)
axes.set_aspect('equal', adjustable='box')
axes.xaxis.labelpad = 20
axes.yaxis.labelpad = 20
axes.patch.set_facecolor('ghostwhite')

fig = plt.gcf()
axes.add_artist(arena)
fig.savefig("../plots/traj.pdf", dpi=900)