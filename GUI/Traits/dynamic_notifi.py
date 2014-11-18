from enthought.traits.api import Float, HasTraits, Instance


class Part(HasTraits):
    cost = Float(2.0)


class Widget(HasTraits):
    part1 = Instance(Part)
    part2 = Instance(Part)
    cost = Float(2.0)

    def __init__(self):
        self.part1 = Part()
        self.part2 = Part()
        self.part1.on_trait_change(self.update_cost, 'cost')
        self.part2.on_trait_change(self.update_cost, 'cost')

    def update_cost(self):
        self.cost = self.part1.cost + self.part2.cost


w = Widget()
w.part1.cost = 2.25
w.part2.cost = 5.31
print w.cost