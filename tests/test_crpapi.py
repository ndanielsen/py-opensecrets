from opensecrets import CRP
from opensecrets.exceptions import CRPError

import pytest

def test_sanity():
    assert 1 + 1 == 2

def test_api_requires_key():
    with pytest.raises(CRPError):
        CRP()
