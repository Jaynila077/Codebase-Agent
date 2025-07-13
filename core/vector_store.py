from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "code_chunks"

def create_collection(dim: int):
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
        )

def upsert_chunks(chunks: list[dict]):
    points = []

    for chunk in chunks:
        points.append(PointStruct(
            id=uuid.uuid4().int >> 64,
            vector=chunk["embedding"],
            payload={
                "filepath": chunk["filepath"],
                "language": chunk["language"],
                "type": chunk["type"],
                "start": chunk["start"],
                "end": chunk["end"],
                "code": chunk["code"]
            }
        ))

    client.upsert(collection_name=COLLECTION_NAME, points=points)

def search_similar(text_embedding: list[float], top_k=5):
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=text_embedding,
        limit=top_k
    )
    return results

