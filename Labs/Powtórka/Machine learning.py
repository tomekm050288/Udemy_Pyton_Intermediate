import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


X, y = make_blobs(n_samples=100, centers=4, cluster_std=0.60, random_state=0)

plt.scatter(X[:,0],X[:,1])

WCSS = []

for k in range(1,15):
    k_means = KMeans(n_clusters = k)
    k_means.fit(X)
    WCSS.append(k_means.inertia_)

plt.plot(range(1,15),WCSS)
plt.xlabel("Number of KMeans clusters")
plt.ylabel("WCSS")
plt.grid()
plt.show()
