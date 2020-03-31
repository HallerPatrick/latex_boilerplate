#! /usr/bin/env python3

import argparse
import pathlib
import os
import shutil
import subprocess
import sys

from colorama import init, Fore


BASE_PATH = "./base"
LATEXBIN = "pdflatex"
PDF_VIEWER = "zathura"



def main():

    init()

    parser = argparse.ArgumentParser(description='Boilerplate generator for latex project.')
    parser.add_argument('destination', type=str, help='Destination folder for latex project')

    args = parser.parse_args()

    base_path = pathlib.Path(BASE_PATH)
    dest_path = pathlib.Path(args.destination)

    if dest_path.exists():
        print(Fore.RED + "Destination already exists.")
        sys.exit(-1)

    print(Fore.GREEN + "Copying latex files to {}...".format(str(dest_path)))
    shutil.copytree(str(base_path), str(dest_path))

    print(Fore.GREEN + "Building project...")
    subprocess.Popen([LATEXBIN, "document.tex"], cwd=str(dest_path))

    print(Fore.GREEN + "Opening pdf...")
    subprocess.Popen([PDF_VIEWER, "document.pdf"], cwd=str(dest_path))





if __name__ == "__main__":
    main()
