class TS(HasTraits):
    data = Array(shape=(None, None))
    fromdate = Date
    todate = Date


# Timeserie view
class TSAdapter(TabularAdapter):
    # link first column of the TS.data array to a column named 'value'
    columns = ['a', 'b', 'c']
    alignment = 'right'
    # format = '%.4f'
    can_edit = True


timeserie_view = View(Item('data',
                           show_label=False,
                           editor=TabularEditor(adapter=TSAdapter(),
                                                editable=True,
                                                operations=['edit', 'insert', 'append'])),
                      title="TS Editor",
                      width=0.9,
                      height=0.9)


def test_ts():
    ts = TS(data=random((10, 3)))
    ts.configure_traits(view=timeserie_view)


if __name__ == '__main__':
    test_ts()