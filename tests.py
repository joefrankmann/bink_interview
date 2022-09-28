import unittest
from unittest.mock import patch
from main import *


class TestClass(unittest.TestCase):
    
    def test_csv_to_list(self):
        func = csv_to_list('./data/dataset.csv')
        self.assertEqual(func[0], ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]', 'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date', 'Lease Years', 'Current Rent'])
        self.assertTrue(func, list)
    
    def test_current_rent_is_in_ascending_order(self):
        func = current_rent()
        func.pop(0)
        lst=[]
        for substring in func:
            lst.append(float(substring[-1]))
        res = lst == sorted(lst)
        self.assertTrue(res)

    def test_lease_years_list_if_is_25(self):
        func = lease_years_list()
        func.pop(0)
        lst=[]
        for substring in func:
            lst.append(int(substring[-2]))
        value=list(dict.fromkeys(lst))
        for v in value:
            res = v
        self.assertEqual(res, 25)

    def test_five_first_items_list(self):
        func = five_first_items()
        func.pop(0)
        size = len(func)
        self.assertEqual(size, 5)
  
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



# squares = []
# for i in range(10):
#     squares.append(i**2)
    
# print(squares)

# squares = [ i**2 for i in range(10)]

# lst=[]
# for substring in func:
#     lst.append(int(substring[-2]))
# lst=[int(substring[-2] for substring in func)]