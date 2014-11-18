from enthought.traits.api import HasTraits, Int, Float, Instance, Property


class Body(HasTraits):
    height = Int(1)
    weight = Int(1)
    bmi = Float()
    # bmi =Property(depend_on=['height,weight'])

    def _height_changed(self, old, new):
        print'The Height change from %s to %s' % (old, new)
        self.bmi = self.height / self.weight

    def _anytrait_changed(self, name, old, new):
        print "The %s change from %s to %s " % (name, old, new)


a = Body()
a.height = 100

