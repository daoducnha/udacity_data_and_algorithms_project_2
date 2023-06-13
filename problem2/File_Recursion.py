import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_paths = list()
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    sub_paths = os.listdir(path)

    for sub_path in sub_paths:
        list_paths.extend(find_files(suffix, os.path.join(path, sub_path)))

    return list_paths

ls = find_files(".c", "testdir")
print(ls)
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3