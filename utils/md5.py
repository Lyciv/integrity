import hashlib


def md5(text):
    md=hashlib.md5(text.encode('utf-8'))
    md5pwd=md.hexdigest()
    return md5pwd