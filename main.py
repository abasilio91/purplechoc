from hashlib import pbkdf2_hmac
from base64 import b64decode, b64encode

def get_low_password(password: str) -> str:
    pass

def get_target(target: str) -> str:
    pass

def get_optional(optional: str) -> str:
    pass

def combine_keys(password: str, target: str, optional: str=None) -> str:
    return target+password+optional

def hash_password(password: str, salt: str) -> str:
    iter = 500_000
    original_key = b64decode(bytes(f'{password+salt}', 'utf-8'))
    enc_key = pbkdf2_hmac('sha256', original_key, bytes(f'{salt}', 'utf-8') * 2, iter)
    return b64encode(enc_key).decode("utf-8")
