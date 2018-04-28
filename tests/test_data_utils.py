from opensecrets import data_utils

import pytest

def test_sanity():
    assert 1 + 1 == 2

def test_get_114_congress_members():
    data = data_utils.get_114_congress_members()
    assert 'CID' in data[0].keys()
    assert 'CRPName' in data[0].keys()
    assert 'Party' in data[0].keys()
    assert 'Office' in data[0].keys()
    assert 'FECCandID' in data[0].keys()

def test_get_113_congress_members():
    data = data_utils.get_113_congress_members()
    assert 'CID' in data[0].keys()
    assert 'CRPName' in data[0].keys()
    assert 'Party' in data[0].keys()
    assert 'Office' in data[0].keys()
    assert 'FECCandID' in data[0].keys()

def test_get_2016_candidates():
    data = data_utils.get_2016_candidates()
    assert 'CID' in data[0].keys()
    assert 'CRPName' in data[0].keys()
    assert 'Party' in data[0].keys()
    assert 'DistIDRunFor' in data[0].keys()
    assert 'FECCandID' in data[0].keys()

def test_get_committee_codes():
    data = data_utils.get_committee_codes()
    assert 'CODE' in data[0].keys()
    assert 'CmteName' in data[0].keys()

def test_get_expenditure_codes():
    data = data_utils.get_expenditure_codes()
    assert 'ExpCode' in data[0].keys()
    assert 'DescripShort' in data[0].keys()
    assert 'DescripLong' in data[0].keys()
    assert 'Sector' in data[0].keys()
    assert 'SectorName' in data[0].keys()

def test_get_industry_codes():
    data = data_utils.get_industry_codes()
    assert 'Catcode' in data[0].keys()
    assert 'Catname' in data[0].keys()
    assert 'Industry' in data[0].keys()
    assert 'Sector' in data[0].keys()
    assert 'Sector Long' in data[0].keys()
