from sys import int_info
import threading
from typing import Mapping

def test(str):
  if str == "t1":
    print(str)
  elif str == "t2":
    print(str)


if __name__ == '__main__':
  t1 = threading.Thread(target=test, args="t1")
  t2 = threading.Thread(target=test, args="t2")

  t1.start
  t2.start
  
