import csv
from datetime import datetime
from operator import itemgetter


dataset = './data/dataset.csv'

def csv_to_list(dataset):
    """Converts CSV file to List"""
    with open(dataset, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        raw_csv_list = list(csv_reader)
        return raw_csv_list

def current_rent():
    """Produces a list sorted by “Current Rent” in ascending order"""
    csv_list = csv_to_list(dataset)
    header = csv_list.pop(0)
    for sublist in csv_list:
        sublist[-1] = float(sublist[-1])
    sorted_list = sorted(csv_list, key=itemgetter(-1))
    for sublist in sorted_list:
        sublist[-1] = str(sublist[-1])
    sorted_list.insert(0,header)
    return sorted_list 

def five_first_items():
    """Returns a list with the five first items of the “Current Rent” list"""
    sorted_list = current_rent()
    return sorted_list[0:6]

def lease_years_list():
    """Returns a list with the Tenants with 25 years lease """
    csv_list = csv_to_list(dataset)
    header = csv_list.pop(0)
    lease_years_index = header.index('Lease Years')
    lease_years_list = []
    for sublist in csv_list:
        if sublist[lease_years_index] == '25':
            lease_years_list.append(sublist)
    lease_years_list.insert(0,header)
    return lease_years_list

def total_rent():
    """Returns the total rent for the list of tenanants with 25 years lease"""
    lease_25_years = lease_years_list()[1:]
    total =[]
    for sublist in lease_25_years:
        sublist[-1] = float(sublist[-1])
        total.append(sublist[-1])
    return sum(total)
    
def dict_tenant_name_and_masts():
    """Returns the Tenants Names and their amount of Masts"""
    csv_list = csv_to_list(dataset)
    header = csv_list.pop(0)
    tenant_index = header.index('Tenant Name')

    tenants = []
    for sublist in csv_list:
        tenants.append(sublist[tenant_index])

    def remove_extra(name):
        return name.split()[0]
    def first_three(name):
        return name[0:3]
    
    tenants_first_name = list(map(remove_extra,tenants))
    tenants_first_three = list(map(first_three,tenants))
    key_words = list(dict.fromkeys(tenants_first_name))
    
    names = []
    for key in key_words:
        index = [idx for idx, s in enumerate(tenants) if key in s][0]
        names.append(tenants[index])
    keys_list = list(dict.fromkeys(names))

    results_dict = {}
    for values in tenants_first_three:
            results_dict[values] = tenants_first_three.count(values)
    values_list = list(results_dict.values())

    final_results = dict(zip(keys_list, values_list))
    return final_results

    
def lease_start_date():
    """Returns a list with the Tenants with 
    “Lease Start Date” between 1st June 1999 and 31st August 2007"""
    csv_list = csv_to_list(dataset)
    header = csv_list.pop(0)
    lease_start_date_index = header.index('Lease Start Date')
   
    start = datetime.strptime('01/06/1999', '%d/%m/%Y')
    end = datetime.strptime('31/08/2007', '%d/%m/%Y')
 
    lease_start_date = []
    for sublist in csv_list:
        sublist[lease_start_date_index] = datetime.strptime(sublist[lease_start_date_index], '%d %b %Y')
        if start <= sublist[lease_start_date_index] <= end:
            sublist[lease_start_date_index] = datetime.strftime(sublist[lease_start_date_index],'%d/%m/%Y')
            lease_start_date.append(sublist)     
    lease_start_date.insert(0,header)
    return lease_start_date

print(lease_start_date())