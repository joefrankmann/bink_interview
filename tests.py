import unittest
from unittest.mock import patch
from main import *

class TestClass(unittest.TestCase):
    
    def test_csv_to_list(self):
        func = csv_to_list('./data/dataset.csv')
        self.assertEqual(func[0], ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]', 'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date', 'Lease Years', 'Current Rent'])
        self.assertTrue(func, list)
    
    def test_current_rent(self):
        func = current_rent()
        self.assertTrue(func, list)

    def test_lease_years_list(self):
        func = lease_years_list()
        self.assertTrue(func, list)
    
    def test_total_rent(self):
        func = total_rent()
        self.assertTrue(func, float)
    
    def test_dict_tenant_name_and_masts(self):
        func = dict_tenant_name_and_masts()
        self.assertTrue(func, dict)
    
    def test_lease_start_date(self):
        func = lease_start_date()
        self.assertTrue(func, list)

    
unittest.main()