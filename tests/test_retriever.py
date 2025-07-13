from core.embedder import embed_code
from core.vector_store import search_similar

query = "Where is the sequences created?"

embedding = embed_code(query)
results = search_similar(embedding)

print("Top results:")
for res in results:
    payload = res.payload
    print(f"{payload['filepath']}:{payload['start']}–{payload['end']}")
    print(payload["code"])
    print("-" * 40)
