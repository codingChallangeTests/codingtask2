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
    }
]

# testing valide data inputs


@pytest.mark.parametrize('test_data', merge_test_data)
def test_merge(test_data):
    out = merge(test_data['intervals'])
    assert out == test_data['result']
