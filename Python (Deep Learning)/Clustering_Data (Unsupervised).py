# Clustering data

# -----------------------

# k-means clustering
from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3)
model.fit(samples)
labels = model.predict(samples)
print(labels)
