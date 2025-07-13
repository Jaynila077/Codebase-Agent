from core.parser import parse_file
from core.chunker import normalize_chunk

chunks = parse_file('data/example_repo/app.py')

for c in chunks:
    norm_chunks = normalize_chunk(c)
    for nc in norm_chunks:
        print(f"[{nc['type']}] {nc['filepath']}:{nc['start']}-{nc['end']} → ID: {nc['id']}")
        print(nc["code"])
        print("-" * 60)
