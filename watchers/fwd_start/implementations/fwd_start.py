#!/usr/bin/env python3

import csv

  
def fwd_start(product):
    if not product.report_date or not product.start_date:
        return False
    
    else:
        if product.start_date > product.report_date:
            if product.trade_date < product.report_date:
                return True
            else:
                return False
        
        # etc.... all edge cases
        
    return False
    
    
# We can create a generic implementation of the tests as follows:
def csv_to_dict(csv):
    """Returns tests in CSV as a dictionary"""
    tests = []

    file_path = 'fwd_start/tests/fwd_start_tests.csv'
    input_file = csv.DictReader(open(file_path))

    for row in input_file:
        tests.append(row)
    
    return tests    
  
def test_fwd_start(csv):
    tests = csv_to_dict(csv)
    for test in tests:
        assert fwd_start(test) == test.fwd_start
        
