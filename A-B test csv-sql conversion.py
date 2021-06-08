# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:10:32 2021

@author: grosa
"""

import csv_to_sqlite


options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
input_file = ['C:/Users/grosa\OneDrive/Desktop/AdSmartABdata - AdSmartABdata.csv']
csv_to_sqlite.write_csv(input_file, "AdsmartABdata.sql", options)


#Get User Input

        