import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class FAISSStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def reset(self):
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add_texts(self, texts):
        if not texts:
            return

        embeddings = self.model.encode(texts, convert_to_numpy=True)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query, k=3):
        if len(self.texts) == 0:
            return []

        query_vec = self.model.encode([query]).astype("float32")

        k = min(k, len(self.texts))  # prevent index error

        distances, indices = self.index.search(query_vec, k)

        results = []

        for i in indices[0]:
            if i == -1:
                continue
            if i < len(self.texts):
                results.append(self.texts[i])

        return results