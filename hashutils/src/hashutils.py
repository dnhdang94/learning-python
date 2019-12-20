import os
import sys
import hashlib

_BLOCK_SIZE = 2 ** 16

def _compute_hexdigest(hash_obj, file_path):
    """
    This is private function to compute checksum for a file.

    -----------
    Parameters:
        hash_obj (obj): hash object that is returned from hashlib (e.g: hashlib.md5(),...).
        file_path (str): full path to file that needs to be generated checksum.

    --------
    Returns:
        str: checksum of target file.
    """

    hasher = hash_obj
    with open(file_path, 'rb') as f:
        buf = f.read(_BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(_BLOCK_SIZE)
    
    return hasher.hexdigest()

def compute_file_md5_hexdigest(path):
    """
    This function generate MD5 checksum for a file.

    -----------
    Parameters:
        path (str): full path to file that needs to be generated checksum.

    --------
    Returns:
        str: checksum of target file.
    """

    md5 = hashlib.md5()
    return _compute_hexdigest(md5, path)

def compute_file_sha1_hexdigest(path):
    """
    This function generate SHA-1 checksum for a file.

    -----------
    Parameters:
        path (str): full path to file that needs to be generated checksum.

    --------
    Returns:
        str: checksum of target file.
    """

    sha1 = hashlib.sha1()
    return _compute_hexdigest(sha1, path)

def compute_file_sha256_hexdigest(path):
    """
    This function generate SHA-256 checksum for a file.

    -----------
    Parameters:
        path (str): full path to file that needs to be generated checksum.

    --------
    Returns:
        str: checksum of target file.
    """

    sha256 = hashlib.sha256()
    return _compute_hexdigest(sha256, path)
