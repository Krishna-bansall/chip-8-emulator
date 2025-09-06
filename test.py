byte = 0x5F
# for bit in byte:
#     print(bit)

for x in range(8):
    if byte & (0x80 >> x):
        print(1)
    else:
        print(0)

print(byte) 