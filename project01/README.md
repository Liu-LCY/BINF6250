# Introduction
In this project, we are focused on parsing a Variant Call Format (VCF) file (`clinvar_20190923_short.vcf`) to analyze genetic variations and their associated phenotypes. The target is to write a Python script that reads the file. 

The project included the script `project01.py`,  and the program extracts specific value pairs from the `INFO` column to identify rare variants, which are defined as having an ExAC allele frequency (`AF_EXAC`) of less than 0.0001. For these rare variants, the code extracts the associated diseases from the `CLNDN` key, and excluding any entries marked as "not_specified" or "not_provided". Then,  it counts the number of times each disease occurs and outputs the results using the `pprint` module.

# Pseudocode


```
FUNCTION parse_line(line):
   columns ← SPLIT(line, "\t")
   pairs   ← SPLIT(columns[INFO], ";")
   lookup  ← {}                       # empty dictionary

   FOR each pair IN pairs:
       key, value ← SPLIT_FIRST(pair, "=")
       IF key is missing OR value is missing:
           CONTINUE
       lookup[key] ← value

   IF "AF_EXAC" NOT IN lookup:
       RETURN []

   af ← TO_NUMBER(lookup["AF_EXAC"])
   IF af ≥ 0.0001:
       RETURN []

   diseases ← SPLIT(lookup["CLNDN"], "|")
   result   ← []

   FOR each d IN diseases:
       IF d ≠ "not_specified" AND d ≠ "not_provided":
           APPEND d TO result

   RETURN result
```
```
FUNCTION read_file(file):
   counts ← {}
   OPEN file
   FOR each line IN file:
       IF line STARTS WITH "#":
           CONTINUE                   # header line
       diseases ← parse_line(line)
       FOR each d IN diseases:
           IF d IN counts:
               counts[d] ← counts[d] + 1
           ELSE:
               counts[d] ← 1
   RETURN counts
```
# Successes
- Read line by line: The program uses a line-by-line reading method (`for line in f:`). This avoids loading the entire VCF file into memory with `readlines()`, allowing it to handle massive genomic datasets.
- GitHub Collaboration: As a team, we managed the fork-and-pull-request workflow. Collaborators successfully forked the leader's repository and committed changes directly to their `project01_PR` branches. We then successfully opened pull requests and merged the collaborators' code into the project leader's repository after review.
- Dictionary-base lookups: Building a key-value dictionary for each line allows the program a lookup process that do not depend on where a key happens to sit. The INFO field can vary between records.
- Robustness details: Using `split("=",1)` ensures that a value containing an additional equals sign "=" does not break the parsing process. The program also skips `INFO` entries that do not contain an equals sign, such as bare flags.
  
# Struggles
Description of the stumbling blocks the team experienced
- Preprocessing - the header filter used a membership test rather than a prefix test. 64 lines contain "#", only 28 start with one.
- Rarity Comparison - which at first was written inverted, returning "[]" for rare variants. It ran without error and produced a dictionary.

# Personal Reflections
## Group Leader
Because I am not very familiar with GitHub, setting up the repository infrastructure was a bit of a struggle for me.  I had some difficulty understanding the workflow for creating the `project01_start` bookmark branch and the `project01_PR` branch. Also, due to some missteps during the branch creation and commit process, my branch ended up being 2 commits ahead of main instead. It took me some time to solve these problems, but it gave me a much clearer understanding of how commits and branching actually work in a collaborative environment.

## Other member
Getting used to all the github branches and the synchronize process with the Group Leader project has its learning curve for sure.

-`What I learned:` I learned how important is checking the repository state before commiting being a important step on the collaborating safety through GitHub.

-`Next Action:` As next steps will be keep using the Github and tool so it can be helping me to improve the knowledge on the github webpage. Also before any commit from the command line I would run the "git status" and "git log --oneline main..HEAD" which would help to confirm the branch state.

Another reflection point are the skills that we need to develop of preprocessing and making sure we are accessing the correct data. It was observed that 64 lines contain "#" but only 28 start with one.

-`What I learned:` Before parsing a file, we need to examine the structure and confirm how headers, fields, and missing values are represented.

-`Next Action:` Getting used to start the prep processing as the first step while analyzing the data counting lines by prefix, checking key presence per record. 

The last point I want to bring is the "Rarity threshold". The project requirements set a variant rare only when "AF_EXAC < 0.0001". If that comparison operation is added in a reversal form it would not represent the correct data output.

-`Evidence and Reasoning:` The inverted comparison on the rarity is a great reasoning point, since the wrong logic side would not get the correct value but would not display a specific error to be fixed. 

-`Next Action:` Test threshold-based conditions to confirm that only values strict below "0.0001" are classified as rare.

# Generative AI Appendix

The appendix entry must contain:
1. Description of which generative AI was used and its version.
   Claude - Opus 5 
2. The entire prompt that was used to generate the content.
   Can you help me to fix my pseudocode to a latex format and the github?  
3. An explanation of how it was used (e.g., to generate ideas).
   It guided me on the correct format github friendly.
4. A justification for why generative AI was used.
   Once I paste the pseudocode on github it was not formatted.
