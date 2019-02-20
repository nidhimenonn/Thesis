#!/usr/bin/env python
# coding: utf-8

# packages i need

import numpy as np
import pandas as pd
import glob
import os
import csv
import re


# dta format


index_file_names = glob.glob('*.dta')


# show the files


index_file_names


# read the files in stata


data = pd.read_stata("demographic_and_other_particulars_of_household_members.dta")


# read other files


data_2 = pd.read_stata('summary of comsumer expenditure.dta')


# taking string and using the dictionary


def pull_files(folder_name):
    """
    INPUTS: Takes in a folder name as a stirng
    OUTPUTS: DataFrame Dictionary
    """
    output = {}
    file_path = folder_name + '/*.dta'
    index_file_names = glob.glob(file_path)
    for file in index_file_names:
        output[file] = pd.read_stata(file)
        print(file + " successfully uploaded, chief")
    return output
    


# using the data dictionary


data_dict = pull_files("Nss64_1.0_type1_new format")


# 2

curr = data_dict["Nss64_1.0_type1_new format/identification of sample household.dta"].head()


# 3


curr.head()


# 4


curr.

