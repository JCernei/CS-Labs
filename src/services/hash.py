import hashlib


def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
