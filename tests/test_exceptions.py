from opensecrets.exceptions import CRPError

import pytest

def test_sanity():
    assert 1 + 1 == 2

def test_exception():
    with pytest.raises(CRPError):
        raise CRPError("Something is broken")
