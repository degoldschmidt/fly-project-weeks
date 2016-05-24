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

x = toSI(data[:,1],params['x'])
y = toSI(data[:,2],params['y'])

fig = figure(figsize=(8.8,8.4))
axes = plt.gca()
plt.xlim([x0+(x0/10),x1+(x1/10)])
plt.ylim([y0+(y0/10),y1+(y1/10)])
lbfs = 16
plt.xlabel('x [mm]', fontsize=lbfs)
plt.ylabel('y [mm]', rotation='horizontal', fontsize=lbfs)
pplt.plot(x, y, 'k.', markersize=2)
axes.set_aspect('equal', adjustable='box')
axes.xaxis.labelpad = 20
axes.yaxis.labelpad = 20
axes.patch.set_facecolor('ghostwhite')

fig = plt.gcf()
axes.add_artist(arena)
fig.savefig("../plots/traj.pdf", dpi=900)

print(data.shape[0], "data points processed.")
dt = 1/120
outdata = np.zeros((data.shape[0],9))
outdata[:,0] = data[:,0]
outdata[:,1] = x
outdata[:,2] = y

dx = np.diff(x)
dx.resize((dx.shape[0]+1,))
dy = np.diff(y)
dy.resize((dy.shape[0]+1,))

outdata[:,3] = np.arctan2(dy, dx)                                       ### PHI

outdata[:-1,4] = np.diff(outdata[:,3])                                  ### dPHI
outdata[:,4] /= dt
outdata[:,5] = np.sqrt(dx*dx + dy*dy)/dt                                ### forward speed
outdata[:-1,6] = np.diff(outdata[:,5])                                  ### forward acceleration
outdata[:,6] /= dt
outdata[:,7] = np.sqrt(x*x+y*y)                                         ### distance from center
outdata[:,8] = np.arctan2(y, x)                                         ### angle of center-fly wrt axis


outfile = "../data/processed/traj_process.dat"
np.savetxt(outfile, outdata, delimiter=' ', newline='\n', fmt='%3.7f %3.6f %3.6f %3.6f %3.6f %3.6f %3.6f %3.6f %3.6f ', header='#t[s] #X[mm] #Y[mm] #phi[rad] #dphi[rad/s] #v[mm/s] #a[mm/s^2] #r[mm] #theta[rad] ')