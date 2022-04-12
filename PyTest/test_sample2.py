import pytest
@pytest.mark.parametrize("input1,input2,output",[(5,5,10),(5,5,9)])
def test_add(input1,input2,output):
    assert input1+input2 == output

#execution:py.test -k test_sample2.py -v