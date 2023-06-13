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

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
print("=============Test case 1=============")
ls = find_files(".c", "testdir")
print(ls)
assert ls == ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
## Test Case 2
print("=============Test case 2=============")
ls = find_files(".h", "testdir")
print(ls)
assert ls == ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']
## Test Case 3
print("=============Test case 3=============")
ls = find_files(".gitkeep", "testdir")
print(ls)
assert ls == ['testdir/subdir4/.gitkeep', 'testdir/subdir2/.gitkeep']
