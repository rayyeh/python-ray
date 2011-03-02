import csv
import sys
import xlwt
from xlwt.Utils import rowcol_to_cell

from optparse import OptionParser

def render_header(ws, fields, first_row=0):
    """
    Generate an Excel Header.

    Builds a header line using different 
    fonts from the default.
    """
    header_style = xlwt.easyxf(
        'font: name Helvetica, bold on')
    col = 0
    for hdr in fields:
        ws.write(first_row, col, hdr, header_style)
        col += 1
    return first_row+2

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--file', help='CSV Data File')
    parser.add_option('-o', '--output', help='Output XLS File')
    opts, args = parser.parse_args()

    if not opts.file or not opts.output:
        parser.error('Input source and output XLS required')

    # Create a dict reader from an open file 
    # handle and iterate through rows.
    reader = csv.DictReader(open(opts.file, 'rU'))

    headers = [field for field in reader.fieldnames if field]
    headers.append('Profit')

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Cost Analysis')

    # Returns the row that we'll start at
    # going forward.
    row = render_header(sheet, headers)

    for day in reader:
        sheet.write(row, 0, day['Date'])
        sheet.write(row, 1, day['Revenue'])
        sheet.write(row, 2, day['Cost'])
        sheet.write(row, 3, 
            xlwt.Formula('%s-%s' % (rowcol_to_cell(row, 1), rowcol_to_cell(row, 2))))
        row += 1            

    # Save workbook
    workbook.save(opts.output)
