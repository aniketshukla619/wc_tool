"""
File operations mapping file.
"""

from file_operations import (
    get_bytes_count,
    get_lines_count,
    get_words_count,
    get_characters_count
)


operations_mapping = {
    "-c" : get_bytes_count,
    "-l" : get_lines_count,
    "-w" : get_words_count,
    "-m" : get_characters_count
}
