# ---
# Golem
# By Sanix-darker
# ----------------

import argparse
from pygolem import *
from phpgolem import *
from jsgolem import *


if __name__ == '__main__':
    # Initialize the arguments
    prs = argparse.ArgumentParser()
    prs.add_argument('-p', '--path', help='Path of the project', type=str, required=True)
    prs.add_argument('-t', '--type', help='The type of the project (php, js, py)', type=str, required=True)
    prs = prs.parse_args()

    if prs.type.lower() == "py":
        pyg = PyGolem(prs.path)
        pyg.generate_app()

