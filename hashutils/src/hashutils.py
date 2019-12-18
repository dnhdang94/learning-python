import os
import sys
import hashlib

_BLOCK_SIZE = 2 ** 16

def _compute_hexdigest(hash_obj, file_path):
    hasher = hash_obj
    with open(file_path, 'rb') as f:
        buf = f.read(_BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(_BLOCK_SIZE)
    
    return hasher.hexdigest()

def compute_file_md5_hexdigest(path):
    md5 = hashlib.md5()
    return _compute_hexdigest(md5, path)

def compute_file_sha1_hexdigest(path):
    sha1 = hashlib.sha1()
    return _compute_hexdigest(sha1, path)

def compute_file_sha256_hexdigest(path):
    sha256 = hashlib.sha256()
    return _compute_hexdigest(sha256, path)
