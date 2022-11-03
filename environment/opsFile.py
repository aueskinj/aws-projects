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
while i <= 23:
    charr[i] = write('Isinsulin-seq-clean.txt')
    i+=1
while i <= 53:
    write(charr[i])
    i+=1
while i <= 88:
    write('Isinsulin.txt') = charr[i]
    i+=1
while i <= 109:
    charr[i] = write('Isinsulin.txt')
    i+=1