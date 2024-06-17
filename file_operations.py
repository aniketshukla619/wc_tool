"""

"""

def get_bytes_count(file_text: str) -> int:
    """
    Count the bytes in the file content
    Args: 
        file_text (str): file content
    Returns:
        int: count of bytes in the file.
    """
    return len(file_text.encode("utf-8"))


def get_words_count(file_text: str) -> int:
    """
    Count the words in the file content
    Args: 
        file_text (str): file content
    Returns:
        int: count of words in the file.
    """
    words = []
    lines = file_text.strip().split("\n")

    for line in lines:
        if line.strip() == "":
            continue
        words.extend(line.strip().split(" "))
    return len(words)


def get_lines_count(file_text: str) -> int:
    """
    Count the lines in the file content
    Args: 
        file_text (str): file content
    Returns:
        int: count of lines in the file.
    """
    lines = file_text.strip().split("\n")
    return len(lines)


def get_characters_count(file_text: str) -> int:
    """
    Count the characters in the file content
    Args: 
        file_text (str): file content
    Returns:
        int: count of characters in the file.
    """
    return len(file_text)
