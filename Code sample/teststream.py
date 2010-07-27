def interact():
    print 'Hello stream world!'
    while 1:
        try:
            reply=raw_input('Enter a number:')
        except EOFError:
            break
        else:
            num=int(reply)
            print "%d squard is %d" %(num,num*num)
    print 'Bye'
    
if __name__=='__main__':
    interact()