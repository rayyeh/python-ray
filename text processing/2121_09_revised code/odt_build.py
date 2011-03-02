#!/usr/bin/python

import sys
import inspect
from collections import namedtuple

from odf.style import Style, TextProperties, ParagraphProperties
from odf.opendocument import OpenDocumentText
from odf.text import P, Span

# Build Global Styles
TYPE_STYLE = Style(name='TYPE_STYLE', family='text')
TYPE_STYLE.addElement(
    TextProperties(
        color='#000000', fontsize='16pt', fontfamily='Helvetica'))

NAME_STYLE = Style(name='NAME_STYLE', family='text')
NAME_STYLE.addElement(
    TextProperties(
        color='#ff0000', fontsize='16pt', fontfamily='Helvetica'))

DOC_STYLE = Style(name='DOC_STYLE', family='paragraph')
DOC_STYLE.addElement(
    TextProperties(
        color='#000000', fontsize='12pt', fontfamily='Helvetica'))
DOC_STYLE.addElement(
    ParagraphProperties(
        marginbottom='16pt', marginleft='14pt'))

# Named tuple makes accessing our returned object
# easier.
ObjectDesc = namedtuple('ObjectDesc', 'name type doc')

def module_members(module):
    """
    Iterates through all of the top-level members
    of a given object and yields an ObjectDesc 
    named tuple. 

    This top-level function acts as a generator.
    """
    def _predicate(obj):
        return (inspect.isclass(obj) 
            or inspect.isfunction(obj))

    # Pull all of the members and yield those
    # that are defined in 'module.' If there's 
    # no docstring, return a placeholder
    members = inspect.getmembers(module, _predicate)
    for name,obj in members:
        if inspect.getmodule(obj) is module:
            yield ObjectDesc(name, type(obj).__name__.title(),
                inspect.getdoc(obj) or 'No Documentation')
        

class ModuleDocumenter(object):
    """
    Documents a module.

    Generates documentation for a module
    in ODT format for all top level 
    elements.
    """
    def __init__(self, module, output=None):
        self._output = output or module.__name__
        self.doc = OpenDocumentText()
        self.module = module
        self._add_styles()

    def _add_styles(self):
        """
        Add Automatic Styles.
        """
        self.doc.automaticstyles.addElement(TYPE_STYLE)
        self.doc.automaticstyles.addElement(NAME_STYLE)
        self.doc.automaticstyles.addElement(DOC_STYLE)

    def _create_header(self, objdef):
        """
        Build the Type/Name Header.
        """
        paragraph = P()
        paragraph.addElement(
            Span(stylename='TYPE_STYLE', text='%s: ' % objdef.type))

        paragraph.addElement(
            Span(stylename='NAME_STYLE', text=objdef.name))

        return paragraph

    def build(self):
        """
        Generate a new ODT file.
        """
        for member in module_members(self.module):

            # Type & Name
            self.doc.text.addElement(
                self._create_header(member))

            # Docstring
            self.doc.text.addElement(
                P(stylename='DOC_STYLE', text=member.doc))

        # Write to file
        self.doc.save(self._output, True)
       

if __name__ == '__main__':
    # Run the documentation system.
    doc = ModuleDocumenter(sys.modules['__main__'], '__main__')
    doc.build()
