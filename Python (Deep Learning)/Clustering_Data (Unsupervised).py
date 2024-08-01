# Clustering data

# -----------------------

# k-means clustering
from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3)
model.fit(samples)
labels = model.predict(samples)
print(labels)
# plotting the kmeans
import matplotlib.pyplot as plt
xs = samples[:,0]
ys = samples[:,2]
plt.scatter(xs,ys, c = labels)
plt.show()
