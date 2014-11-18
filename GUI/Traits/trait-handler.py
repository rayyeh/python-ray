# -*- coding:utf-8 -*-
from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.menu import *
from enthought.traits.ui.wx import *


class SayHi(HasTraits):
    hi = Str
    hi = 'I am Here'
    myview = View(Item('hi', style='readonly', show_label=False),
                  kind='modal',
                  title="Say Hi to all",
                  buttons=OKCancelButtons
    )


class Personal_Handler(Handler):
    my_button = Button('Say hi')

    def _my_button_changed(self, info):
        hello = SayHi()
        #hello.configure_traits()
        hello.edit_traits()


    def do_recalc(self, info):
        print 'Press do_recalc'

    def do_op1(self, info):
        print 'Menu op1'

    def do_op2(self, info):
        print 'Menu op2'

    def do_tool1(self, info):
        print 'tool1 Show'


class Personal(HasTraits):
    first_name = Str()
    last_name = Str()
    year = Int()
    my_list = Str()
    single_date = Date
    print_button = Button()
    dir = Directory()
    file = File()
    #shell=object
    current = Bool

    def _first_name_changed(self):
        self.last_name = self.first_name

    def _print_button_changed(self):
        self.first_name = 'Ray'
        self.last_name = 'Yeh'

    def _single_date_changed(self):
        print self.single_date

    recalc = Action(name="Recalculate", action='do_recalc')
    menu_1 = Action(name='op1', action='do_op1')
    menu_2 = Action(name='op2', action='do_op2')
    tool1 = Action(name='Tool1', action='do_tool1', tooltip='tooltip')

    view1 = View(Group(
        Item('dir', editor=DirectoryEditor(), label=u'目錄', show_label=True),
        Item('file', editor=FileEditor(), label=u'檔案', show_label=True),
        #Item('shell',editor=ShellEditor()),
        Item('first_name', editor=TextEditor()),
        Item('last_name', style='simple'),
        Group(Item('single_date', label=u'開始日期', show_label=True),
              Item('single_date', label=u'結束日期', show_label=True),
              orientation='horizontal'
        ),

        Item('handler.my_button', show_label=False),
        #editor=ButtonEditor(label="Mybutton")),
        Group(
            Item('my_list', editor=CheckListEditor( \
                values=['op1', 'op2', 'op3'])),
            Item('print_button', show_label=False)
        ),
        label='External view',
        show_border=True,
        show_labels=False
    ),
                 menubar=MenuBar(Menu(menu_1, menu_2, name='My Menu')), toolbar=ToolBar(tool1),
                 handler=Personal_Handler,
                 buttons=[OKButton, CancelButton, recalc],
                 title="Trait Handle.py",
                 kind='nonmodal'
    )


if __name__ == "__main__":
    a = Personal()
    a.configure_traits(view='view1')

    print '--------End------------'


