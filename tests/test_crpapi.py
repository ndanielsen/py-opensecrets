
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from opensecrets import CRP
from opensecrets.exceptions import CRPError
import os

import pytest

def test_sanity():
    assert 1 + 1 == 2

def test_api_requires_key():
    # @mock.patch.dict(os.environ,{'DATABASE_URL':'mytemp'})
    with patch.dict(os.environ, {'OPENSECRETS_API_KEY': ''}):
        with pytest.raises(CRPError):
            CRP()
