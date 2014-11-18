import binascii

F63 = {}


def setVbv(eci, cavv, xid):
    tag = '99'
    size = binascii.a2b_hex('0043')
    value = size + eci + binascii.a2b_hex(cavv) + binascii.a2b_hex(xid)
    tsize = 45
    F63[tag] = [tsize, size, value]
    return F63


def setID(id):
    tag = 'ID'
    size = binascii.a2b_hex('0012')
    value = size + tag + id.upper()
    tsize = 14
    F63[tag] = [tsize, size, value]
    return F63


def setCvv(ind, resp, cvv):
    tag = '16'
    size = binascii.a2b_hex('0008')
    value = size + tag + str(ind) + str(resp) + cvv.ljust(4, ' ')
    tsize = 10
    F63[tag] = [tsize, size, value]
    return F63


F63 = setID('a123456789')
F63 = setCvv(1, 0, '123')
print F63

i = F63_size = 0
F63_value = ''
for i in F63:
    F63_size += F63[i][0]
    F63_value += F63[i][2]

print 'F63_value:', binascii.b2a_hex(F63_value)
print 'F63_size:', F63_size