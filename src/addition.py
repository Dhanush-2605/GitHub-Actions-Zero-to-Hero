# app.py
# This is a test commit
# CICD test
def add(a, b):
    return a + b

def demo():
    print("hi")

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
