# WRITING BINARY FILES MANUALLY
with open('binary', 'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))


# removing the for loop
with open('binary', 'bw') as binfile:
    binfile.write(bytes(range(12)))


# READING BINARY FILES
with open('binary', 'br') as binFile:
    for b in binFile:
        print(b)



