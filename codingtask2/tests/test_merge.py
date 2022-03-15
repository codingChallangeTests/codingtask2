import pytest

from codingtask2.merge import merge

merge_test_data = [
    {
        'intervals': [[25, 30], [2, 19], [14, 23], [4, 8]],
        'result': [[2, 23], [25, 30]],
    },
    {
        'intervals': [[-11, 30], [2, 19], [14, 23], [4, 8]],
        'result': [[-11, 30]],
    },
    {
        'intervals': [[1, 1]],
        'result': [[1, 1]],
    },
    {
        'intervals': [[1, 1.55], [1.33, 1.66]],
        'result': [[1, 1.66]],
    },
    {
        'intervals': [[25, 30], [2, 19], [14, 23], [4, 8], [25, 30], [2, 19], [14, 23], [4, 8]],
        'result': [[2, 23], [25, 30]],
    },
    {
        'intervals': [],
        'result': [],
    },
]

#testing valide data inputs
@pytest.mark.parametrize('test_data', merge_test_data)
def test_merge(test_data):
    out = merge(test_data['intervals'])
    assert out == test_data['result']


# testing invalid data inputs
def test_merge_error_1():
    with pytest.raises(TypeError) as exc_info:
        merge("foobar")
    assert str(exc_info.value) == 'intervals type != list'


def test_merge_error_2():
    with pytest.raises(ValueError) as exc_info:
        merge([[1, 2], [9, 1]])
    assert exc_info.value.args[0] == 'invalid interval data input'
    assert exc_info.value.args[1] == [9, 1]


def test_merge_error_3():
    with pytest.raises(TypeError) as exc_info:
        merge([['a', 2], [0, 1]])

def test_merge_error_4():
    with pytest.raises(TypeError) as exc_info:
        merge([[True, 2], [0, 1]])
    assert exc_info.value.args[0] == 'invalid interval data type input'
    assert exc_info.value.args[1] == [True, 2]

def test_merge_error_5():
    with pytest.raises(IndexError) as exc_info:
        merge([[2], [0, 1]])

def test_merge_error_6():
    with pytest.raises(IndexError) as exc_info:
        merge([[], [0, 1]])

def test_merge_error_7():
    with pytest.raises(TypeError) as exc_info:
        merge([None, [9, 1]])
    assert exc_info.value.args[0] == "'NoneType' object is not subscriptable"

def test_merge_error_8():
    with pytest.raises(TypeError) as exc_info:
        merge([False, [9, 1]])
    assert exc_info.value.args[0] == "'bool' object is not subscriptable"

def test_merge_error_9():
    with pytest.raises(TypeError) as exc_info:
        merge([10, [9, 1]])
    assert exc_info.value.args[0] == "'int' object is not subscriptable"