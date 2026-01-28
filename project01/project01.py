#!/usr/bin/env python3
"""
Group 1: Tien Nguyen, Fardina Tabassum, Shameem Shahib
Project 01: Functional File Parsing
"""

from collections import defaultdict
from pprint import pprint
from typing import Optional, List

# pylint: disable=too-many-return-statements
def parse_line(line:str) -> Optional[List[str]]:
    """
    - Take string as argument
    - If AF_EXAC is not present, skip the line, return None
    - If AF_EXAC is rare (< 0.0001), return a list of diseases in CLNDN
    (does not include not_specified & not_provided)
    - if AF_EXAC is not rare, return empty list
    """

    rare_cutoff = 0.0001
    clndn_ignore = {"not_specified", "not_provided"}

    line = line.strip()
    #skip metadata and header line
    if line.startswith('#'):
        return None

    #values are tab separated and make up of 8 columns
    cols = line.split('\t')
    if len(cols) < 8:
        return None

    #index of INFO is 7
    info = cols[7]
    info_dict = {}

    #build info dictionary
    for entry in info.split(';'):
        if '=' in entry:
            #key-value separated by "="
            key, value = entry.split('=',1)
            info_dict[key.strip()] = value.strip()

    if  "AF_EXAC" not in info_dict:
        return None

    try:
        af_exac = float(info_dict["AF_EXAC"])
    except ValueError:
        return None

    if af_exac >= rare_cutoff:
        return []

    if "CLNDN" not in info_dict:
        return []

    #the diseases are pipe (|) separated
    diseases = info_dict["CLNDN"].split("|")

    count_d = []
    for disease in diseases:
        disease = disease.strip()
        #make sure disease is not "" and not in clndn_ignore
        if disease and disease not in clndn_ignore:
            count_d.append(disease)

    return count_d

def read_file(vcf_path:str) -> dict:
    """
    - Take string as argument (vcf_path)
    - open file
    - read line by line
    - call and use parse_line function
    - use dictionary to count result given from parse_line function
    - return the dictionary
    """
    counts = defaultdict(int)

    with open(vcf_path, 'r', encoding='utf-8') as vcf:
        for line in vcf:
            diseases = parse_line(line)

            if diseases is None:
                continue

            for disease in diseases:
                counts[disease] += 1

    return dict(counts)

if __name__ == '__main__':
    #Business Logic
    pprint(read_file("clinvar_20190923_short.vcf"))
