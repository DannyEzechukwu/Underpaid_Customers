#import variables from accounting.py
from accounting import * 

#define function with the input of a file name

def order_report_automation(filename): 
    """Return a message if the expected total of a customer is not equal to 
    what customer actually paid

    Arguments:
        - filename (str): the path to a data file

    Return:
        - str: what the customer paid vs what the expected payment was
    """
    customer_report = open(filename)
    customer_report_list = []
    for line in customer_report:
        line = line.strip()
        line = line.split('|')
        del line[0]
        customer_report_list.append(line) # [['first_name last_name', melons_purchased, amount_paid]]
    
    customers_who_paid_more_or_less = []
    for line in customer_report_list: 
        if float(line[2]) != float(line[1]) * melon_cost: 
            customers_who_paid_more_or_less.append(f"{line[0]} paid ${line[2]}, expected ${float(line[1]) * melon_cost}")

    for statement in customers_who_paid_more_or_less:
        print(statement, "\n")

    
order_report_automation('customer-orders.txt')