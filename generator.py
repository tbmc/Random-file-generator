import os
import secrets
import random
import string
from typing import Optional, Union, cast, Set, Tuple


name_length_limits = 5, 50
file_content_length_limits = 100, 100 * 10 ** 6


def generate_random_secure(length: int) -> bytes:
    return secrets.token_bytes(length)


def generate_random(length: int) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def generate_random_file(
    folder_path: str, name: Union[int, str, None], content_length: Union[None, int, Tuple[int, int]]
) -> None:
    """
    This will overwrite file if it exists
    """
    if type(name) is str:
        name = cast(str, name)
    else:
        if type(name) is int:
            name = cast(int, name)
            name = generate_random(name)
        if not name:
            name_length = random.randint(*name_length_limits)
            name = generate_random(name_length)

    if content_length:
        if type(content_length) is tuple:
            content_length = cast(Tuple[int, int], content_length)
            content_length = random.randint(*content_length)
    else:
        content_length = random.randint(*file_content_length_limits)

    content = generate_random_secure(content_length)
    name = cast(str, name)
    file_path = os.path.join(folder_path, name)
    with open(file_path, "wb") as file:
        file.write(content)


def generate_random_files(
    folder_path: str, nbr_files: int, content_length: Union[None, int, Tuple[int, int]]
) -> None:
    names: Set[str] = set()

    for i in range(nbr_files):
        name = ""
        while len(name) == 0 and name not in names:
            name_length = random.randint(*name_length_limits)
            name = generate_random(name_length)

        names.add(name)
        generate_random_file(folder_path, name, content_length)
