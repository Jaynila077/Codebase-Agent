import hashlib
import tiktoken

def build_chunk(base_chunk, code_block, index=None):
    raw_id = code_block.encode()
    hash_id = hashlib.sha256(raw_id).hexdigest()[:16]

    if index is not None:
        hash_id = f"{hash_id}-{index}"

    return {
        "id": hash_id,
        "type": base_chunk["type"],
        "filepath": base_chunk["filepath"],
        "language": base_chunk["language"],
        "start": base_chunk["start"],
        "end": base_chunk["end"],
        "code": code_block.strip()
    }

# def approx_token_count(text: str) -> int:
#     return len(text.split())

enc = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str):
    return len(enc.encode(text))  

def normalize_chunk(chunk, max_tokens=256):
    code = chunk["text"].strip()
    token_count = count_tokens(code)

    if token_count <= max_tokens:
        return [build_chunk(chunk, code)]

    lines = code.splitlines()
    subchunks = []
    current_block = []

    for line in lines:
        current_block.append(line)
        if count_tokens("\n".join(current_block)) >= max_tokens:
            subchunks.append("\n".join(current_block))
            current_block = []

    if current_block:
        subchunks.append("\n".join(current_block))

    return [build_chunk(chunk, sub, i) for i, sub in enumerate(subchunks)]
