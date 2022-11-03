infile = 'preproinsulin-seq.txt'
outfile = 'preProinsulin-seq.txt'

delete_list = ["//", "ORIGIN", "1", "61"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)