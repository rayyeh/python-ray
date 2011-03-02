import sys
import random
from lxml import etree

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
        self.opened = []

    def init_game(self):
        """
        Process World XML.
        """
        self.location = etree.parse(self.world).getroot()

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
            print "You've encountered a %s!" % monster.get('kind')
            max_dmg = int(monster.get('max_dmg'))
            min_dmg = int(monster.get('min_dmg'))
            self._decr_hp(random.randint(min_dmg, max_dmg))

    def _open_chest(self, chest):
        """
        Open a treasure chest.
        """
        self.opened.append(chest)
        modifier = self.get_nodes('trap', chest) or self.get_nodes('potion', chest)
        if not modifier:
            print "This chest is empty..."
        else:
            modifier = modifier[0]
            hp_change = int(modifier.get('hp'))
            if modifier.tag == 'trap':
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
                closed_chests = [i for i in chests if i not in self.opened]
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
        if parent is None:
            parent = self.location

        return parent.xpath(name)

    def get_description(self, node):
        """
        Returns a description for an object.
        """
        return ''.join(node.xpath('description/text()')).strip()

    @property
    def parent(self):
        parent = self.location.xpath('..')
        return parent[0] if parent else None
    
    def advance(self, where):
        """
        Move into the next room.

        Moves the player into the next room and handles
        whatever consequences have been defined in the
        dungeon.xml file.
        """
        self.location = where
        print '%s... %s' % (where.tag.title(), 
            self.get_description(where))

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
            exits[i.get('direction')] = i

        directions = exits.keys()
        if self.parent is not None:
            directions.append('back')

        while True:
            choice = raw_input("Advance? [%s]: " % ', '.join(directions))
            if choice:
                if choice == 'back' and 'back' in directions:
                    self.advance(self.parent)
                try:
                    self.advance(exits[choice])
                except KeyError:
                    print "That's a brick wall. Try again."

def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-w', '--world',
        help='Dungeon Definition XML')
    opts, args = parser.parse_args()
    
    if not opts.world:
        parser.error("World XML Required")

    a = Adventure(opts.world)
    a.init_game()
    try:
        a.start_game()
    except YouDiedError, e:
        print str(e)
    except (EOFError, KeyboardInterrupt):
        print "Until next time..."

