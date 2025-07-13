from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("BAAI/bge-small-en")  

def embed_code(text: str) -> list[float]:
    embedding = MODEL.encode(text, convert_to_numpy=True).tolist()
    return embedding


def embed_chunks(chunks: list[dict]) -> list[dict]:
    embedded = []
    for chunk in chunks:
        embedding = embed_code(chunk["code"])
        chunk["embedding"] = embedding
        embedded.append(chunk)
    return embedded

