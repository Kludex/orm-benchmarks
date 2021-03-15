import os
import time
from random import choice

from models import Journal
from pony.orm import commit, db_session

LEVEL_CHOICE = [10, 20, 30, 40, 50]
count = int(os.environ.get("ITERATIONS", "1000"))


start = now = time.time()
with db_session():
    for i in range(count):
        Journal(level=choice(LEVEL_CHOICE), text=f"Insert from B, item {i}")
    commit()
now = time.time()

print(f"Pony ORM, B: Rows/sec: {count / (now - start): 10.2f}")
