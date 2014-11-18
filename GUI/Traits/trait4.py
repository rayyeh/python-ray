# -*- coding:utf-8 -*-
# trait4.py -- example DelegatesTo 
from enthought.traits.api import *

import enthought.traits.ui


class Parent(HasTraits):
    last_name = Str
    first_name = Str


class Child(HasTraits):
    first_name = Str
    last_name = DelegatesTo('father')
    age = Int
    father = Instance(Parent)
    monther = Instance(Parent)

    def _age_changed(self, old, new):
        print 'Agent chagne %s to %s ' % (old, new)


tony = Parent(first_name="A", last_name="B")
alice = Parent(first_name="C", last_name="D")

sally = Child(age=10, father=tony, monther=alice)
print sally.last_name
sally.last_name = 'XXX'
print sally.last_name


# PrototypedFrom example
class P(HasTraits):
    first_name = Str
    family_name = ''
    favorite_first_name = Str
    child_allowance = Float(1.00)


class C(HasTraits):
    __prefix__ = 'child_'
    first_name = PrototypedFrom('mother', 'favorite_*')
    last_name = PrototypedFrom('father', 'family_name')
    allowance = PrototypedFrom('father', '*')
    father = Instance(P)
    mother = Instance(P)


fred = P(first_name='Fred', family_name='Lopes', \
         favorite_first_name='Diego', child_allowance=5.0)

maria = P(first_name='Maria', family_name='Gonzalez', \
          favorite_first_name='Tomas', child_allowance=10.0)

nino = C(father=fred, mother=maria)
print '%s %s gets $%.2f for allowance' % (nino.first_name, nino.last_name, nino.allowance)
    


    