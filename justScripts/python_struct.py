from struct import *

packed_data = pack('iif', 6,19,4.73)

print(packed_data)
print(calcsize('i'))
print(calcsize('f'))

unpack_data = unpack('iif', packed_data)
print(unpack_data)