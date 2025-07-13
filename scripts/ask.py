from core.embedder import embed_code
from core.vector_store import search_similar
from core.prompt_builder import build_prompt
from core.inference import ask_llm

import sys

query = sys.argv[1]

embedding = embed_code(query)
results = search_similar(embedding, top_k=4)

prompt = build_prompt(query, [r.payload for r in results])
answer = ask_llm(prompt)

print("Answer:")
print(answer)
