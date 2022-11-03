# #for getting rid of unwanted characters
# infile = 'preproinsulin-seq.txt'
# outfile = 'preProinsulin-seq.txt'
# delete_list = ["//", "ORIGIN", "1", "61", " "]
# with open(infile) as fin, open(outfile, "w+") as fout:
#     for line in fin:
#         for word in delete_list:
#             line = line.replace(word, "")
#         fout.write(line)
        
#for counting number of chars
f = open('preproinsulin-seq-clean.txt')
data = f.read()
numChar = len(data)
print("number of characters is: {}".format(numChar))

#for saving the first 24 ammino acids
charr = f.readline()
i = 0
def writefc(name, end, start):
    fin = open('preproinsulin-seq-clean.txt')
    charr = fin.readline()
    fout = open(name, "w")
    i = start - 1
    while i < end:
        fout.write(charr[i])
        i += 1

writefc('Isinsulin-seq-clean.txt', 24, 1)
writefc('binsulin-seq-clean.txt', 53, 25)
writefc('cinsulin-seq-clean.txt', 89, 54)
writefc('ainsulin-seq-clean.txt', 110, 90)