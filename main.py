import sys
from typing import Optional

import generator


if __name__ == "__main__":
    """
    0: path of the script
    1: number of files to generate
    2: path
    3: content length
    """
    assert len(sys.argv) >= 2
    nbr = int(sys.argv[1])
    path = "."
    if len(sys.argv) >= 2:
        path = sys.argv[2]

    content_length: Optional[int] = None
    if len(sys.argv) >= 3:
        content_length = int(sys.argv[3])

    generator.generate_random_files(path, nbr, content_length)
