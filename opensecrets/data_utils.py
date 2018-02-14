import csv
import itertools
import os

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

def _read_csv(file_path, num_skip_rows=0):
    """Opens the CSV file_path given a file path, returns a list of dictionaries

    Parameters
    --------

    file_path : str
        file path location

    num_skip_rows : int, optional
        number of header rows to skip
    """

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(itertools.islice(csv_file, num_skip_rows, None))
        return list(csv_reader)

def _construct_file_path(file_name):
    """Constructs a file path to files location in the data directory """
    return os.path.join(DATA_DIR, file_name)

def get_114_congress_members(file_path=None):
    """ Returns key information for 114th Congress members in list of python dictionaries

    Contains: CID, CRPName, Party, Office, FECCandID
    """

    if file_path is None:
        file_path = _construct_file_path('crp-members-114.csv')
    return _read_csv(file_path, num_skip_rows=1)

def get_113_congress_members(file_path=None):
    """ Returns key information for 113th Congress members in list of python dictionaries

    Contains: CID, CRPName, Party, Office, FECCandID
    """

    if file_path is None:
        file_path = _construct_file_path('crp-members-113.csv')
    return _read_csv(file_path, num_skip_rows=1)

def get_2016_candidates(file_path=None):
    """ Returns key information for US National candidates for 2016

    Contains: CID, CRPName, Party, DistIDRunFor, FECCandID
    """
    if file_path is None:
        file_path = _construct_file_path('crp-candidateIDs-2016.csv')
    return _read_csv(file_path, num_skip_rows=1)

def get_committee_codes(file_path=None):
    """List of Congressional Committes and their abbreviation

    Contains: CODE, CmteName
    """
    if file_path is None:
        file_path = _construct_file_path('crp-congressional-committee-codes.csv')
    return _read_csv(file_path, num_skip_rows=0)

def get_expenditure_codes(file_path=None):
    """List of Expenditure codes along with additional information

    Contains: ExpCode, DescripShort, DescripLong, Sector, SectorName
    """

    if file_path is None:
        file_path = _construct_file_path('crp-expenditure-codes.csv')
    return _read_csv(file_path, num_skip_rows=1)

def get_industry_codes(file_path=None):
    """List of Categories for Industries

    Contains: Catcode, Catname, Catorder, Industry, Sector, Sector Long
    """

    if file_path is None:
        file_path = _construct_file_path('crp-industry-codes.csv')
    return _read_csv(file_path, num_skip_rows=1)
