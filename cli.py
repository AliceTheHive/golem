# ---
# Golem-cli
# By Sanix-darker
# ----------------

import argparse
from utils import *

if __name__ == '__main__':
    # Initialize the arguments
    # Example of command line : python3 cli.py -p ./test_app -t py
    prs = argparse.ArgumentParser()
    prs.add_argument('-p', '--path', help='The path of the code/project.', type=str, required=True)
    prs.add_argument('-t', '--type', help='The type of the code/project.', type=str, required=True)
    prs.add_argument('-n', '--name', help='The name of the code/project.', type=str, default="golem_test_app")
    prs = prs.parse_args()

    generate_app(prs.path, prs.type, prs.name)
