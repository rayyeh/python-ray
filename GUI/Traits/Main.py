# -*- coding:utf-8 -*-
from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.menu import *
from enthought.traits.ui.file_dialog \
    import open_file


class SayHi(HasTraits):
    hi = Str
    hi = 'I am Here'
    myview = View(Item('hi', style='readonly', show_label=False),
                  #kind='modal',
                  title="Say Hi to all",
                  buttons=OKCancelButtons
    )


class MainWindow(HasTraits):
    first_name = Str()
    last_name = Str()
    year = Int()
    my_list = Str
    single_date = Date
    print_button = Button()
    my_button = Button('Popup say hi')
    dir = Directory
    file_name = File(value='d://install.ini')
    text_context = Str()
    #shell=object
    current = Bool

    def _first_name_changed(self):
        self.last_name = self.first_name

    def _print_button_changed(self):
        self.first_name = 'Ray'
        self.last_name = 'Yeh'

    def _single_date_changed(self):
        print self.single_date

    def _my_button_changed(self):
        hello = SayHi()
        hello.edit_traits()

    def do_recalc(self):
        print 'Press do_recalc'

    def _file_name_changed(self, old, new):
        print '_file_name_changed'
        self.file_name = new
        self.text_context = open(self.file_name, 'rU').read()

    def file_open(self):
        print 'file open'
        #x=open_file()        
        #self.text_context=open(name,'rU').read()               

    def file_close(self):
        print 'Menu op2'

    def do_tool1(self):
        print 'tool1 Show'


    recalc = Action(name="Recalculate", action='do_recalc')
    menu_1 = Action(name='Open', action='file_open')
    menu_2 = Action(name='Close', action='file_close')
    tool1 = Action(name='Tool1', action='do_tool1', tooltip='tooltip')

    view1 = View(Group(
        Item('dir', editor=DirectoryEditor(entries=1), label=u'目錄', show_label=True),
        Item('file_name', editor=FileEditor(entries=1), label=u'檔案', show_label=True),
        Item('text_context', editor=TextEditor(), style='custom', resizable=True, show_label=True),
        #Item('shell',editor=ShellEditor()),
        Item('first_name', editor=TextEditor(), show_label=True),
        Item('last_name', style='simple', show_label=True),

        Group(Item('single_date', label=u'開始日期', show_label=True),
              Item('single_date', label=u'結束日期', show_label=True),
              #orientation='horizontal',
              show_border=True
        ),

        Group(
            Item('my_list', editor=CheckListEditor( \
                values=['op1', 'op2', 'op3'])),
            Item('print_button', show_label=False),
            spring,
            Item('my_button', show_label=False),
            #editor=ButtonEditor(label="Mybutton")),
            show_border=True,
        ),
        label='External view',
        show_border=True,
        show_labels=False,
    ),
                 menubar=MenuBar(Menu(menu_1, menu_2, name='File'), Menu(menu_2, name='Edit')),
                 toolbar=ToolBar(tool1),
                 #handler=Personal_Handler,
                 buttons=[OKButton, CancelButton, recalc],
                 title="Trait Handle.py",
                 kind='nonmodal',
                 id='grouping',
                 resizable=True
    )

    view2 = View(VSplit(
        Tabbed(
            Item('dir', editor=DirectoryEditor(), label=u'目錄', show_label=False),
            Item('file', editor=FileEditor(), label=u'檔案', show_label=False),
            Item('text_context', editor=TextEditor(), style='readonly', resizable=True),
            #Item('shell',editor=ShellEditor()),
            Item('first_name', editor=TextEditor(), show_label=True),
            Item('last_name', style='simple', show_label=True)
        ),
        Tabbed(
            Item('single_date', label=u'開始日期', show_label=True),
            Item('single_date', label=u'結束日期', show_label=True),
            #orientation='horizontal',
            show_border=True
        ),
        VGroup(
            Item('my_list', editor=CheckListEditor( \
                values=['op1', 'op2', 'op3'])),
            Item('print_button', show_label=False),
            spring,
            spring,
            Item('my_button', show_label=False),
            show_border=True,
            #dock='horizontal'
            #orientation='horizontal'
        ),

        label='External view',
        show_border=True,
        show_labels=False
    ),

                 menubar=MenuBar(Menu(menu_1, menu_2, name='File'), Menu(menu_2, name='Edit')),
                 toolbar=ToolBar(tool1),
                 #handler=MainWindow_Handler,
                 buttons=[OKButton, CancelButton, recalc],
                 title="Trait Handle.py",
                 kind='nonmodal',
                 id='vsplit',
                 resizable=True
    )


if __name__ == "__main__":
    a = MainWindow()
    a.configure_traits(view='view1')

    print '--------End------------'


