from scipy import spatial

# Find the distance between each embedding
def get_pairwise_dist(embeddings):
    return spatial.distance.squareform(spatial.distance.pdist(embeddings, metric="cosine"))
