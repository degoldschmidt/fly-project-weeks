import numpy as np
import matplotlib.pyplot as plt  ## package for plotting
import seaborn as sns
import prettyplotlib as pplt  ## package for plotting

def dropnan(x): 
    return x[~np.isnan(x)]

data = np.loadtxt("../data/processed/traj_process.dat", skiprows=1)  

fig, ax = plt.subplots()
ax.set_xlim((-np.pi, np.pi))
ax.set_xticks([-np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi])
ax.set_xticklabels([ '-$\pi$', '$\pi/2$', '0', '$\pi/2$', '$\pi$'])
plt.hist(dropnan(data[:,3]),32, normed=1, facecolor='dodgerblue')

plt.savefig("../plots/hist.pdf", dpi=900)