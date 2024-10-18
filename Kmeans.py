# Correcting the Manhattan distance calculation
# Updated K-Means algorithm for clustering
import numpy as np
# Given points and initial cluster centers
points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])
initial_centers = np.array([[2, 10], [5, 8], [1, 2]])

# Distance function using Manhattan distance (L1 norm)
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

# K-Means algorithm function
def kmeans(points, initial_centers, iterations):
    centers = initial_centers
    for _ in range(iterations):
        clusters = [[] for _ in range(len(centers))]
        
        # Assign points to the nearest center
        for point in points:    
            distances = [manhattan_distance(point, center) for center in centers]
            nearest_center = np.argmin(distances)
            clusters[nearest_center].append(point)
        
        # Recalculate the centers as the mean of the points in each cluster
        new_centers = []
        for cluster in clusters:
            if cluster:  # Avoid empty clusters
                new_centers.append(np.mean(cluster, axis=0))
            else:
                new_centers.append(centers[len(new_centers)])
        
        centers = np.array(new_centers)
    
    return centers, clusters

# Running the K-Means algorithm for 2 iterations
final_centers, final_clusters = kmeans(points, initial_centers, iterations=2)

print(final_centers, final_clusters)
print(f'The Final Centers for the K means Classifier',final_centers,"and the Final clusters are ",final_clusters)