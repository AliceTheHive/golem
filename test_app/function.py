import json
from os import system as ss


def jdump(json_t):
    print(json.dumps(json_t))


def jloads(json_s):
    print(json.loads(json_s))
