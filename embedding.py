from sentence_transformers import SentenceTransformer
import tensorflow_hub as hub
import numpy as np
from sklearn.decomposition import TruncatedSVD

MAX_COMPONENTS = 50

def normalize(enc):
    # We normalize embeddings so that the average magnitude of vectors is 1
    return  enc / (np.linalg.norm(enc, axis=1).mean())

def encode_text(text_list):
    # Load models
    sbert_model = SentenceTransformer("bert-large-nli-mean-tokens")
    use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

    # Get embeddings
    sbert_embedding = sbert_model.encode(text_list, show_progress_bar=True)
    use_embedding = use_model(text_list).numpy()

    # Concatenate embeddings together
    concat_embedding = np.concatenate([use_embedding, sbert_embedding], axis=1)

    # Initialise SVD to reduce dimensionality
    n_components = min([MAX_COMPONENTS, conat_embedding.shape[0], conat_embedding.shape[1]])
    svd = TruncatedSVD(n_components=n_components)

    return svd.fit_transform(concat_embedding)
