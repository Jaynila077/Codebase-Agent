import os
from core.languages import python

LANGUAGE_HANDLER_MAP = {
    'python': python.extract_chunks,
}

LANGUAGE_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.rs': 'rust',
}

def detect_language(file_path: str):
    for ext, lang in LANGUAGE_MAP.items():
        if file_path.endswith(ext):
            return lang
    return None

def load_code_file(root_dir: str, supported_ext=None):
    if supported_ext is None:
        supported_ext = list(LANGUAGE_MAP.keys())

    files = []
    for root, _, filenames in os.walk(root_dir):
        for f in filenames:
            if any(f.endswith(ext) for ext in supported_ext):
                files.append(os.path.join(root, f))
    return files

def parse_file(file_path: str):
    lang = detect_language(file_path)
    if lang not in LANGUAGE_HANDLER_MAP:
        return []

    with open(file_path, 'rb') as f:
        code = f.read()

    handler = LANGUAGE_HANDLER_MAP[lang]
    chunks = handler(code)

    for chunk in chunks:
        chunk["filepath"] = file_path
        chunk["language"] = lang

    return chunks
