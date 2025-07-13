from core.parser import parse_file
from core.chunker import normalize_chunk
from core.embedder import embed_chunks

chunks = parse_file("data/example_repo/app.py")
all_norm = []

for c in chunks:
    all_norm.extend(normalize_chunk(c))

embedded_chunks = embed_chunks(all_norm)

print("First chunk embedding (first 10 dims):")
print(embedded_chunks[0]["embedding"][:10])
