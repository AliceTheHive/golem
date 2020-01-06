# A list of usefull functions and methods
# utils.py

from pygolem import *
from phpgolem import *
from jsgolem import *


def generate_app(_path, _type, stxt=None, INSERT=None):

    if _type.lower() == "py":
        pyg = PyGolem(_path, stxt, INSERT)
        pyg.generate_app()

    elif _type.lower() == "js":
        jsg = JsGolem(_path, stxt, INSERT)
        jsg.generate_app()

    elif _type.lower() == "php":
        phpg = PhpGolem(_path, stxt, INSERT)
        phpg.generate_app()

    else:
        print("[+] This language is not handle by Golem")
