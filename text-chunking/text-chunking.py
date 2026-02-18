from itertools import islice

def text_chunking(tokens, chunk_size, overlap):
    step = chunk_size - overlap
    chunks = [
        list(islice(tokens, i, i + chunk_size))
        for i in range(0, len(tokens) - chunk_size + 1, step)
    ]
    return chunks if chunks else [tokens] if tokens else []