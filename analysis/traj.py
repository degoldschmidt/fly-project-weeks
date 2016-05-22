import numpy as np
import matplotlib.pyplot as plt  ## package for plotting
import seaborn as sns
import prettyplotlib as pplt  ## package for plotting

plt.close('all')

mydt = np.dtype([ ('name', np.str_, 16), 
                 ('id', np.str_, 1), 
                 ('x', np.int),
                 ('y', np.int),
                 ('size', np.int),
                 ('secsize', np.int) ] )
data = np.loadtxt("../data/fly1.csv", skiprows=1)   
params = np.genfromtxt('../data/processed/arena.cfg', skip_header=1, dtype=mydt)

print(params)

#plt.ylim([-0.25,N-0.75])         ### ONLY RASTER
#plt.ylim([-100,10])
#plt.ylim([-100,N-0.75])
plt.xlim([0,1280])
plt.ylim([0,960])
#plt.ylabel('Neuron index')
#plt.xlabel('Time (msec)')
plt.plot(data[:,1], data[:,2], 'k.', markersize=2)
plt.savefig("./traj.pdf", dpi=900)