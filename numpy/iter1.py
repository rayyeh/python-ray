def column_iterator(target_file, column_number):
    """A generator function for CSV files.
    When called with a file name target_file (string) and column number 
    column_number (integer), the generator function returns a generator 
    which steps through the elements of column column_number in file
    target_file.
    """
    file=open(target_file,'r')
    lines=file.readlines()
    del lines[0]
    for line in lines:
        words=line.split(',')        
        word=words[column_number-1]
        yield word    
    file.close()
    
dates = column_iterator('./table2.csv', 1) 

for date in dates:
    print date

