import numpy as np
import matplotlib.pyplot as plt  ## package for plotting
import seaborn as sns
import prettyplotlib as pplt  ## package for plotting

data = np.loadtxt("../data/processed/traj_process.dat", skiprows=1)  

pplt.plot(data[:,0], data[:,5])
plt.savefig("../plots/orient.pdf", dpi=900)