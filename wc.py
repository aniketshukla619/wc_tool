"""
wc tool implemented in python.
"""

# Library imports
import os
import sys
from collections import defaultdict
from typing import List, Dict
from file_operations_mapping import (
    operations_mapping
)

# to count the total operations for all the files
total = defaultdict(int)

def get_print_string(operations_count_dict: Dict[str, int]) -> str:
    """
    Function responsible to print the value in specified format
    Args:
        operations_count_dict (Dict) : File count dict containing key as operations
                                       and values as count for that operation.
    Returns:
        String: Values in the form of string.
    """
    count_values = operations_count_dict.values()
    print_string = ""

    for value in count_values:
        print_string += "\t" + str(value)

    return print_string

def check_file(filename: str) -> int:
    """
    Checks and validates the filename
    Args:
        filename (str) : Argument filename
    Returns:
        int: exit code 0:Success 1:Unsuccess
    """
    if not (os.path.exists(filename) and os.path.isfile(filename) \
            and os.access(filename, os.R_OK)):
        print(f"wc: {filename}: open: No such file or directory")
        return 1

    return 0

def separate_operations(args: str) -> List[str]:
    """
    Responsible to separate the operations if 
    the operations are combined in the input.
    Args:
        args: combined input arguments

    """
    all_operations = []

    # remove the "-" from the args
    all_chars = args[1:]

    for chars in all_chars:
        all_operations.append("-" + chars)

    return all_operations

def get_file_text(filename: str) -> str:
    """
    Responsible to return the text of the file
    Args:
        filename (str) : input file name.
    Returns:
        str: File content
    """
    f_obj = open(file=filename, mode="r", encoding="utf-8")
    file_content = f_obj.read()
    return file_content

def process_operations(operations: List[str], file_text: str) -> str:
    """ 
    Responsible to process the operations
    on the file content.
    Args:
        operations (list): list of operations to be performed on file content.
        file_text (str) : Content of the file.
    Returns:
        str: Operations result in the form of string. 
    """

    file_counts = { operation: 0 for operation in operations }

    for operation in operations:
        operation_count = operations_mapping[operation](file_text=file_text)
        total[operation] += operation_count
        file_counts[operation] = operation_count

    print_string = get_print_string(file_counts)
    return print_string

def parse_cmd(cmd: List[str]) -> tuple[List[str], List[str]]:
    """
    Parses the cmd and returns the files and operations list.
    Args:
        cmd (list) : command line arguments in the form of list
    Returns:
        Tuple(list, list): Return operations and files list
    """
    default_operations = ["-l", "-w", "-c"]
    operations = []
    files = []

    # starting the index from 1
    # ignoring the python file name
    list_idx = 1

    # parsing operations from the cmd
    while list_idx < len(cmd) and cmd[list_idx].startswith("-"):
        if len(cmd[list_idx]) > 2:
            operations.extend(separate_operations(cmd[list_idx]))
        else:
            operations.append(cmd[list_idx])
        list_idx += 1

    # parsing files from the cmd
    while list_idx < len(cmd) and not cmd[list_idx].startswith("-"):
        files.append(cmd[list_idx])
        list_idx += 1

    if not operations:
        operations = default_operations

    return operations, files

def main():
    """
    Main Function
    """
    sys_args = sys.argv
    operations, files = parse_cmd(sys_args)

    # parsing operations from the command line
    # If empty the base arguments would be
    # check if the arguments passed is a file
    # and if not terminate the program
    if STD_INP:
        output = process_operations(operations, STD_INP)
        print(output)
    else:
        for filename in files:
            exit_code = check_file(filename)
            # if exit code is 1 exit the process
            if exit_code:
                continue

            file_text = get_file_text(filename=filename)
            output = process_operations(operations, file_text)
            output += "\t" + filename
            print(output)

        if len(files) > 1:
            print_string = get_print_string(total)
            print_string += "\t" + "total"
            print(print_string)


if __name__ == "__main__":
    STD_INP = ""
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        STD_INP += line
    main()
