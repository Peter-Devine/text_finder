from sentence_transformers import SentenceTransformer
import tensorflow_hub as hub
import numpy as np

def normalize(enc):
    # We normalize embeddings so that the average magnitude of vectors is 1
    return  enc / (np.linalg.norm(enc, axis=1).mean())

def encode_text(text_list):
    sbert_model = SentenceTransformer("bert-large-nli-mean-tokens")
    use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

    sbert_embedding = sbert_model.encode(text_list, show_progress_bar=True)
    use_embedding = use_model(text_list).numpy()

    return np.concatenate([use_embedding, sbert_embedding], axis=1)
