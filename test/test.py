from example.src.math_operation import add,sub
print("example is imported")
def test_add():
    print("add test begain")
    assert add(2,3)==5
    assert add(1,2)==3
    print("add test end")

def test_sub():
    print("sub test start")
    assert sub(3,1)==2
    assert sub(5,2)==3
    print("sub test end")

if __name__=="__main__":
    test_add()
    test_sub()

