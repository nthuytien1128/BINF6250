# Introduction
This project focuses on parsing a ClinVar Variant Call Format (VCF) file to identify rare genetic variants and tally the diseases associated with those variants. Using Python, the program reads the VCF file line by line to ensure memory efficiency, extracts allele frequency information (AF_EXAC) to determine rarity, and collects disease names from the CLNDN field while excluding unspecified entries. The final output is a dictionary showing how frequently each disease appears among rare variants.

# Pseudocode
Put pseudocode in this box:

```
FUNCTION parse_line(line):
    IF line starts with "#":
        return None

    split line by tab into columns
    extract INFO column

    create empty dictionary info_dict
    FOR each entry in INFO split by ";":
        IF entry contains "=":
            split into key and value
            store in info_dict

    IF AF_EXAC not in info_dict:
        return None

    convert AF_EXAC value to float
    IF conversion fails:
        return None

    IF AF_EXAC >= rare cutoff:
        return empty list

    IF CLNDN not in info_dict:
        return empty list

    split CLNDN by "|"
    remove empty values and ignored disease names
    return list of valid diseases


FUNCTION read_file(vcf_path):
    create empty dictionary counts

    open VCF file
    FOR each line in file:
        diseases = parse_line(line)

        IF diseases is None:
            continue

        FOR each disease in diseases:
            increment count in dictionary

    return dictionary of disease counts


MAIN:
    call read_file on clinvar_20190923_short.vcf
    pretty-print the resulting dictionary
```

# Successes
Successfully implemented line-by-line file reading, avoiding loading the entire VCF file into memory.

Correctly parsed the INFO field using key–value logic instead of relying on fixed positions.

Applied defensive programming techniques to handle missing or malformed data.

Learned how to use tools such as pylint to identify and address code quality issues.

Produced clean, readable, and modular code using functions.

# Struggles
Understanding the structure of the VCF INFO field and how to safely extract specific keys.

Managing multiple return cases in a single function while keeping the logic readable.

Resolving pylint warnings related to return statements and unused strings.

Distinguishing between when to skip a line (None) versus returning an empty list ([]).

Initial setup and correct

# Personal Reflections
## Tien Nguyen (Team leader)
As the group leader, this project reinforced for me how critical clear function design and defensive programming are when working with real biological data formats like VCFs. Leading discussions around logic choices such as how to handle missing or incomplete annotations deepened my understanding of both Python control flow and the structure of the VCF specification. Working through pylint warnings during debugging also pushed me to think more carefully about code readability, consistency, and long term maintainability, rather than just making the script work.

## Fardina Tabassum
This project taught me a lot about text parsing, such as converting text to dictionaries as well as how to optimize memory use by not reading the text line by line. It was a bit challenging to work with GitHub branches at first, but it encouraged a collaborative environment to work in. The project also helped explore different ways to filter out data and was a good refresher on how to handle data.

## Shameem Shahib
I found this project to be both challenging and enriching. Working through the parse_line function and read_file afterwards was a clear process thanks so the pseudocode which laid out the plan for our program. I also had aid from AI to understand the task better and that also helped me approach this with a sense of direction on what I'm being asked and how to do it.
# Generative AI Appendix
Generative AI (ChatGPT) was used as a learning aid during this project. It was consulted to:

Clarify the VCF file format and ClinVar-specific fields

Debug Python syntax and logic errors

Understand pylint warnings and best practices

Improve code readability and structure

All final code, logic decisions, and written content were reviewed and understood by the team. The AI was used in accordance with the course syllabus as a supportive tool rather than a replacement for independent work.
