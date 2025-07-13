from tree_sitter_languages import get_parser

parser = get_parser("python")

def extract_chunks(code_bytes: bytes):
    tree = parser.parse(code_bytes)
    root_node = tree.root_node

    chunks = []

    def walk(node):
        if node.type in ("function_definition", "class_definition","import_statement", "expression_statement", "assignment"):
            chunks.append({
                "type": node.type,
                "start": node.start_point[0] + 1,
                "end": node.end_point[0] + 1,
                "text": code_bytes[node.start_byte:node.end_byte].decode()
            })
        for child in node.children:
            walk(child)

    walk(root_node)
    return chunks
