import string
import random

characters = string.ascii_letters + string.digits + "_-"


def gen_slug():
    return "".join(random.choices(characters, k=10))
