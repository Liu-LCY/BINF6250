"""
BINF6250 Homework Assignment 1
Author: Graziano Peregrino, Congyuan Liu
"""
# !/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(line: str) -> list:
    """
    Parse one VCF data line and return disease names for rare variants.
    @param line: A tab-separated VCF data line in the format:
        CHROM POS ID REF ALT QUAL FILTER INFO.
        The Info column contains semicolon-separated key-value pairs,
        incluing AF_EXAC=float and CLNDN=disease1|disease2.
    @return: List of disease names from CLNDN if AF_EXAC is less than
        0.0001.
        Returns an empty list if AF_EXAC is missing, the variant is not rare,
        or only not_specified/not_provided diseases are found.
    """
    columns = line.split("\t")
    pairs = columns[7].split(";")

    dictionary = {}

    for pair in pairs:
        split_pair = pair.split("=", 1)
        if len(split_pair) != 2:
            continue
        dictionary[split_pair[0]] = split_pair[1]

    if "AF_EXAC" not in dictionary:
        return []

    else:
        af_exac = float(dictionary["AF_EXAC"])
        if af_exac >= 0.0001:  # Rare threshold 0.0001
            return []
        else:
            clndn = dictionary["CLNDN"].split("|")
            final_list = []

            for disease in clndn:
                if disease not in ("not_specified", "not_provided"):
                    final_list.append(disease)

            return final_list


# Modify this function signature and fill in the details
def read_file(filename: str) -> dict:
    """
    Read a VCF file line by line and count rare variant diseases.

    @param filename: Path to a VCF file containing metadata/header lines
        starting with "#" and tab-separated data lines in the format:
        CHROM POS ID REF ALT QUAL FILTER INFO.
    @return: Dictionary with disease names as keys and the number of times
        each disease appears in rate variants as values.
    """
    counts = {}
    with open(filename) as f:
        for line in f:
            # skip lines that start with "#"
            if line.startswith("#"):
                continue
            diseases = parse_line(line)

            for disease in diseases:
                # using get to handle missing keys
                counts[disease] = counts.get(disease, 0) + 1
    return counts


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
