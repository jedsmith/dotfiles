#!/usr/bin/env python3

from hashlib import sha1
from importlib import import_module
from os import stat
from os.path import expanduser, sep
from shutil import copy2
from sys import stderr

def magic(name):
    # converts a_b_c to a/b.c; the last _ is always a dot, the rest pathseps
    *path, last = name.split('_')
    return '{}.{}'.format(sep.join(path), last)

config = import_module('config')
for rdst, src in filter(lambda both: not both[0].startswith('_'), vars(config).items()):
    source, dest = expanduser(src), magic(rdst)
    try:
        source_stat = stat(source)
    except FileNotFoundError:
        print(f"skipping: cannot locate source file: {src}", file=stderr)
        continue
    try:
        dest_stat = stat(dest)
    except FileNotFoundError:
        pass
    else:
        source_sha = sha1(open(source, 'rb').read()).digest()
        dest_sha = sha1(open(dest, 'rb').read()).digest()
        if source_sha == dest_sha:
            print(f"skipping: identical to upstream: {dest}", file=stderr)
            continue
    print(f"copying: {source} -> {dest}")
    copy2(source, dest)