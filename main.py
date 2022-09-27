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
    """Ascending list sorted by “Current Rent”"""
    csv_list = csv_to_list(dataset)
    header = csv_list.pop(0)
    rent_index = header.index('Current Rent')
    for sublist in csv_list:
        sublist[rent_index] = float(sublist[rent_index])
    sorted_list = sorted(csv_list, key=itemgetter(-1))
    for sublist in sorted_list:
        sublist[rent_index] = str(sublist[rent_index])
    sorted_list.insert(0,header)
    return sorted_list

def five_first_items():
    """List five first items of the “Current Rent”"""
    sorted_list = current_rent()
    return sorted_list[0:6]


def lease_years_list():
    """List tenants with 25 years lease"""
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
    """Returns the total rent with 25 years lease"""
    lease_25_years = lease_years_list()[1:]
    total =[]
    for sublist in lease_25_years:
        sublist[-1] = float(sublist[-1])
        total.append(sublist[-1])
    return sum(total)


def dict_tenant_name_and_masts():
    """Dict: Tenants Names and amount of Masts"""
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
    """Lease Start Date btw 1/6/99-31/08/07"""
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


if __name__ == '__main__':
    choice = ''
    while choice != '0':
        print("\n[1] 'Current Rent' in ascending order")
        print("[2] Obtain first 5 items of 'Current Rent'")
        print("[3] Mast data with 'Lease Years' = 25 years")
        print("[4] Total rent for all items in mast data = 25 years")
        print("[5] Tenant name and count of masts for each tenant")
        print("[6] Rentals with Lease Start Date btw 1/6/99-31/08/07")
        print("[all] Show all results above")
        print("[0] Exit")
        
        choice = input("\nChoose one option: ")
        
        if choice == '1':
            print(current_rent())
        elif choice == '2':
            print(five_first_items())
        elif choice == '3':
            print(lease_years_list())
        elif choice == '4':
            print(total_rent())
        elif choice == '5':
            print(dict_tenant_name_and_masts())
        elif choice == '6':
            print(lease_start_date())
        elif choice == 'all':
            print(current_rent())
            print(five_first_items())
            print(lease_years_list())
            print(total_rent())
            print(dict_tenant_name_and_masts())
            print(lease_start_date())
        elif choice == '0':
            pass
        else:
            print("\nWrong option, please try again.\n")
    print("Bye.")