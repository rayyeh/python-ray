import sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from reportlab.lib import colors

class PDFBuilder(object):
    HEIGHT = defaultPageSize[1]
    WIDTH = defaultPageSize[0]

    def _intro_style(self):
        """Introduction Specific Style"""
        style = getSampleStyleSheet()['Normal']
        style.fontName = 'Helvetica-Oblique'
        style.leftIndent = 64
        style.rightIndent = 64
        style.borderWidth = 1
        style.borderColor = colors.black
        style.borderPadding = 10 
        return style

    def __init__(self, filename, title, intro):
        self._filename = filename
        self._title = title
        self._intro = intro
        self._style = getSampleStyleSheet()['Normal']
        self._style.fontName = 'Helvetica'

    def title_page(self, canvas, doc):
        """
        Write our title page.
        
        Generates the top page of the deck, 
        using some special styling.
        """
        canvas.saveState()
        canvas.setFont('Helvetica-Bold', 18)
        canvas.drawCentredString(
            self.WIDTH/2.0, self.HEIGHT-180, self._title)
        canvas.setFont('Helvetica', 12)
        canvas.restoreState()

    def std_page(self, canvas, doc):
        """
        Write our standard pages.
        """
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.drawString(inch, 0.75*inch, "%d" % doc.page)
        canvas.restoreState()

    def create(self, content):
        """
        Creates a PDF.

        Saves the PDF named in self._filename.
        The content paramter is an iterable; each 
        line is treated as a standard paragraph.
        """
        document = SimpleDocTemplate(self._filename)
        flow = [Spacer(1, 2*inch)]

        # Set our font and print the intro
        # paragraph on the first page.
        flow.append(
            Paragraph(self._intro, self._intro_style()))
        flow.append(PageBreak())
           
        # Additional content
        for para in content:
            flow.append(
                Paragraph(para, self._style))
            
            # Space between paragraphs.
            flow.append(Spacer(1, 0.2*inch))

        document.build(
            flow, onFirstPage=self.title_page,
                onLaterPages=self.std_page)


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print "Usage: %s <output> <title> <intro file> <content file>" % \
            sys.argv[0]
        sys.exit(-1)
   
    # Do Stuff
    builder = PDFBuilder(
        sys.argv[1], sys.argv[2], open(sys.argv[3]).read())

    # Generate the rest of the content from a text file
    # containing our paragraphs.
    builder.create(open(sys.argv[4]))
