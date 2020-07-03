import os
import secrets
import random
import string
from typing import Optional


name_length_limits = 5, 50
file_content_length_limits = 100, 100 * 10**6


def generate_random_secure(length: int) -> bytes:
    return secrets.token_bytes(length)


def generate_random(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_file(folder_path: str, extension: Optional[str], name_length: Optional[int], content_length: Optional[int]) -> None:
    """
    This will overwrite file if it exists
    """
    if not name_length:
        name_length = random.randint(*name_length_limits)
    name = generate_random(name_length)
    if not content_length:
        content_length = random.randint(*file_content_length_limits)
    content = generate_random_secure(content_length)
    if extension:
        name += "." + extension
    file_path = os.path.join(folder_path, name)
    with open(file_path, "wb") as file:
        file.write(content)

