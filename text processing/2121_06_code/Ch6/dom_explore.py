import sys
import random
from xml.dom.minidom import parse

__metaclass__ = type

class YouDiedError(Exception):
    """Our Adventure has ended..."""

# World holds dungeons and information
# regarding our adventure.
class Adventure:
    def __init__(self, world, hp=35):
        self.location = None
        self.hp = hp
        self.world = world

    def init_game(self):
        """
        Process World XML.
        """
        self.location = parse(open(self.world)).documentElement

    def start_game(self):
        """
        Starts the game.
        """
        self.advance(self.location)

    def _decr_hp(self, change):
        """
        Lower HP.

        Lower's HP and takes getting killed
        into account.
        """
        self.hp -= change
        print "You have taken %d points of damage!" % change
        if self.hp <= 0:
            raise YouDiedError("You have expired...")
        
        print "You have %d HP remaining." % self.hp

    def _manage_monster(self):
        """
        Handle monster hits.
        """
        monster = self.get_nodes('monster')
        if monster:
            monster = monster[0]
            print "You've encountered a %s!" % monster.getAttribute('kind')
            max_dmg = int(monster.getAttribute('max_dmg'))
            min_dmg = int(monster.getAttribute('min_dmg'))
            self._decr_hp(random.randint(min_dmg, max_dmg))

    def _open_chest(self, chest):
        """
        Open a treasure chest.
        """
        chest.opened = True

        modifier = self.get_nodes('trap', chest) or self.get_nodes('potion', chest)
        if not modifier:
            print "This chest is empty..."
        else:
            modifier = modifier[0]
            hp_change = int(modifier.getAttribute('hp'))
            if modifier.nodeName == 'trap':
                print self.get_description(modifier)
                self._decr_hp(hp_change)
            else:
                print "You've found a potion!"
                print "Health restored by %d HP!" % hp_change
                self.hp += hp_change

    def _manage_chests(self):
        """
        Handle Treasure Chests.
        """
        chests = self.get_nodes('chest')
        if chests:

            while True:
                closed_chests = [i for i in chests if not hasattr(i, 'opened')]
                if closed_chests:
                    chest_count = len(closed_chests)
                    print "There is %d unopened chest(s) here!" % chest_count
                    choice = raw_input("Open which? [%s, none]: " % \
                        ', '.join([str(i) for i in xrange(chest_count)]))

                    if choice == "none":
                        break

                    try:
                        self._open_chest(closed_chests[int(choice)])
                    except (ValueError, IndexError):
                        pass

                # No chests left.
                else:
                    break
   
    def get_nodes(self, name, parent=None):
        """
        Search the DOM Tree.

        Searches the DOM tree and returns nodes
        of a specific name with a given parent.
        """
        if not parent:
            parent = self.location
        return [node for node in parent.getElementsByTagName(name)
                    if node.parentNode is parent]

    def get_description(self, node):
        """
        Returns a description for an object.
        """
        desc = self.get_nodes('description', node)
        if not desc:
            return ''
        desc = desc[0]
        return ''.join(
            [n.data.strip() for n in desc.childNodes if n.nodeType == node.TEXT_NODE])

    def advance(self, where):
        """
        Move into the next room.

        Moves the player into the next room and handles
        whatever consequences have been defined in the
        dungeon.xml file.
        """
        self.location = where
        print '%s... %s' % (where.nodeName.title(), self.get_description(where))

        # Exit if this is the end.
        if self.get_nodes('exit'):
            print "You have won."
            sys.exit(0)

        # Perform monster logic.
        self._manage_monster()

        # Perform Chest Logic
        self._manage_chests()
       
        # Setup available directions menu.
        exits = {}
        for i in self.get_nodes('hallway') + self.get_nodes('room'):
            exits[i.getAttribute('direction')] = i

        directions = exits.keys()
        if self.location.parentNode:
            directions.append('back')

        while True:
            choice = raw_input("Advance? [%s]: " % ', '.join(directions))
            if choice:
                if choice == 'back' and 'back' in directions:
                    self.advance(self.location.parentNode)
                try:
                    self.advance(exits[choice])
                except KeyError:
                    print "That's a brick wall. Try again."
            
if __name__ == '__main__':
    a = Adventure('world00.xml')
    a.init_game()
    try:
        a.start_game()
    except YouDiedError, e:
        print str(e)
    except (EOFError, KeyboardInterrupt):
        print "Until next time..."

