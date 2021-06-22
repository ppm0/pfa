import os
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, getmtime, join
from pathlib import Path
from shutil import copy2


def pfa(source: str, destination: str, quiet: bool, dry_run: bool) -> None:
    files = [(f, getmtime(join(source, f))) for f in listdir(source) if isfile(join(source, f))]
    files.sort(key=lambda f: f[1])
    if not dry_run:
        Path(destination).mkdir(parents=True, exist_ok=True)
    i = 1
    for (f, t) in files:
        s = join(source, f)
        d = join(destination, f'{i:03}_{f}')
        if not quiet:
            print(f'{s} -> {d}')
        if not dry_run:
            copy2(s, d)
        i += 1
    if not dry_run:
        for (f, t) in files:
            s = join(source, f)
            if not quiet:
                print(f'remove {s} -> {d}')
            os.remove(s)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--destination', required=True)
    parser.add_argument('--quiet', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    pfa(**(args.__dict__))
