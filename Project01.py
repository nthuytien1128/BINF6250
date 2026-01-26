#!/usr/bin/env python
from pprint import pprint

def parse_line(line):
    #skips header lines with #
    if line.startswith("#"):
        return[]

    #Information is split by tabs into columns(cols)
    cols = line.split("\t")

    #Extract the column for AF_EXAC
    inf_col = cols[7]

    #Turn information into a dictionary
    inf_dict = {}
    for item in inf_col.split(";"):
        key, value = item.split("=", 1)
        inf_dict[key] = value

    #Check if AF_EXAC is present in the dictionary
    if "AF_EXAC" not in inf_dict:
        return[]

    #turn the value into a float
    af_exac = float(inf_dict["AF_EXAC"])
    if af_exac >= 0.0001:
        return[]

    #Ignore anything with no disease information
    if "CLNDN" not in inf_dict:
        return[]

    #Split diseases
    diseases = inf_dict["CLNDN"].split("|")

    #Filter disease labels
    filtered_disease = []
    for d in diseases:
        if d not in ("not_specified", "not_provided"):
            filtered_disease.append(d)
    return filtered_disease

    pass


# Modify this function signature and fill in the details
def read_file(filename):
    #create dictionary of diseases
    disease_counts = {}
    with open(filename, "r") as f:
        for line in f:
            diseases = parse_line(line)
            for disease in diseases:
                #count diseases
                disease_counts[disease] = disease_counts.get(disease, 0) + 1
    return disease_counts
    pass


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))

    
