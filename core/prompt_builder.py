TEMPLATE = """
You are an expert codebase assistant. Given some source code and a user query, answer clearly and concisely.

### Code Context
{context}

### User Question
{question}

### Your Answer
"""

def build_prompt(question: str, context_chunks: list[dict]) -> str:
    context = "\n\n".join([c["code"] for c in context_chunks])
    return TEMPLATE.format(context=context, question=question)
