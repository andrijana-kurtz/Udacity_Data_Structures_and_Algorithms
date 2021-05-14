'''
Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().
'''
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
    if len(suffix) == 0 or not os.path.isdir(path):
        return []

    results = []
    stack = [path]

    while stack:
        fp = stack.pop()
        if os.path.isfile(fp):
            if suffix == fp[-len(suffix):]:
                results.append(fp)
        else:
            for fs_object in os.listdir(fp):
                stack.append(f'{fp}/{fs_object}')

    return results


assert(find_files('.c', './testdir') == ['./testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c'])
assert(find_files('.c', '') == []) # empty path string
assert(find_files('.c', 'asdf') == []) # non existant path string
assert(find_files('', './testdir') == []) # empty suffix
assert(find_files('.nemame', './testdir') == []) # non existant suffix
