a = 65534
b = 65535
c = 65536 
d = 2998302

# WRITE
with open('binary2', 'bw') as binary2:
    binary2.write(a.to_bytes(2, 'big'))
    binary2.write(b.to_bytes(2, 'big'))
    binary2.write(c.to_bytes(4, 'big'))
    binary2.write(d.to_bytes(4, 'big'))
    binary2.write(d.to_bytes(4, 'little'))

# READ a,b,c,d into e,f,g,h
with open('binary2', 'br') as binary2:
    e = int.from_bytes(binary2.read(2), 'big') # the byte order must be the same as the writing time
    print(e)
    f = int.from_bytes(binary2.read(2), 'big')
    print(f)
    g = int.from_bytes(binary2.read(4), 'big')
    print(g)
    h = int.from_bytes(binary2.read(4), 'big')
    print(h)
    i = int.from_bytes(binary2.read(4), 'little')  # the byte order must be the same as the writing time
    print(i)
