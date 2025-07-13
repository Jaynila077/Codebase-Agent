from core.parser import parse_file
from core.chunker import normalize_chunk
from core.embedder import embed_chunks
from core.vector_store import create_collection, upsert_chunks

import os

def ingest_repo(path):
    all_chunks = []

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                chunks = parse_file(os.path.join(root, f))
                for chunk in chunks:
                    all_chunks.extend(normalize_chunk(chunk))

    embedded_chunks = embed_chunks(all_chunks)
    create_collection(dim=len(embedded_chunks[0]["embedding"]))
    upsert_chunks(embedded_chunks)

if __name__ == "__main__":
    ingest_repo("data/example_repo")
    print("Codebase embedded and stored in Qdrant.")

