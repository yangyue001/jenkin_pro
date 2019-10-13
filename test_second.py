import pytest
import allure

def tes_add(a,b):
    c = a + b
    print("%d + %d is %d"%(a,b,c))
    return c

def test_case01():
    assert tes_add(3,4) == 7


