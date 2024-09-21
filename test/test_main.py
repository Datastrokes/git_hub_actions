
'''import os
from pathlib import Path
import sys
path=Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(path))'''

from src.math_operation import add,sub
print("example is imported")
def test_add():
    assert add(2,3)==5
    assert add(1,2)==3


def test_sub():

    assert sub(3,1)==2
    assert sub(5,2)==3




