
import sys
import getopt


def main():

    filein = open(sys.argv[1], "r")
    print sys.argv[1]
    datain = filein.readlines()
    fileout = open(sys.argv[1]+"-N", "w")
    y = ''
    for i in datain:
        y = y + i
    z = y.replace(' ', '')

    a = z.replace("\n", '')
    msg = ''
    for i in range(0, len(a), 4):
        data = a[i:i + 4]
        if data[3:4] != ':':
            'print data'
            if data[2:3] == ' ':
                msg = msg + data[0:3]
            else:
                msg = msg + data

    x = msg[6:]
    newmsg = x.decode('hex')
    fileout.write(newmsg)
    fileout.close

if __name__ == '__main__':
    main()
