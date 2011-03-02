import sys
import random
from xml.sax import parse
from xml.sax.handler import ContentHandler

__metaclass__ = type

class YouDiedError(Exception):
    """Our Adventure has ended..."""

class Description:
    """A Game Element Description"""

class GameElement:
    """A Game Component"""
    descr = None
    def __str__(self):
        return 'A %s... %s' % \
            (self.__class__.__name__, self.descr if self.descr else '')

class Navigatable(GameElement):
    def __init__(self, parent):
        self.exits = {}
        self.parent = None
        self.is_exit = False
        self.monster = None
        self.chests = []
        if parent:
            self.parent = parent

    def add_exit(self, direction, where):
        self.exits[direction] = where

class Dungeon(Navigatable):
    """Main Dungeon Level"""

class Exit(GameElement):
    """A Dungeon Exit"""

class Hallway(Navigatable):
    """A Hallway Passage"""

class Room(Navigatable):
    """A Room"""

class HPModifier(GameElement):
    """A Non-Monster Modifier"""
    def __init__(self, hp):
        self.hp = hp

class Trap(HPModifier):
    """A Negative HPModifier"""

class Chest(GameElement):
    """A Treasure Chest"""
    opened = False
    contents = None

class Potion(HPModifier):
    """A Positive HP Modifier"""

# Dictionaries map XML names to classes which
# contain relevant information.
NAV_MAP = { 'room': Room, 'hallway': Hallway, 'dungeon': Dungeon }
HP_MAP = { 'trap': Trap, 'potion': Potion }

class Monster:
    def __init__(self, kind, max_dmg, min_dmg):
        self.kind = kind
        self.max_dmg = max_dmg
        self.min_dmg = min_dmg

    def __str__(self):
        return self.kind

    def hit(self):
        """
        Generate damange.

        Returns an HP number randomly pulled from between
        this monster's min and max.
        """
        return random.randint(self.min_dmg, self.max_dmg)

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
        parse(open(self.world), GameHandler(self))

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
        monster = self.location.monster
        if monster:
            print "You've encountered a %s!" % monster
            self._decr_hp(monster.hit())

    def _open_chest(self, chest):
        """
        Open a treasure chest.
        """
        chest.opened = True
        if not chest.contents:
            print "This chest is empty..."
        else:
            modifier = chest.contents
            self.hp += modifier.hp
            if isinstance(modifier, Trap):
                print modifier.descr
                self._decr_hp(modifier.hp)

            # It's a potion
            else:
                print "You've found a potion!"
                print "Health restored by %d HP!" % modifier.hp
                self.hp += modifier.hp

    def _manage_chests(self):
        """
        Handle Treasure Chests.
        """
        if self.location.chests:

            while True:
                closed_chests = [i for i in self.location.chests if not i.opened]
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
    
    def advance(self, where):
        """
        Move into the next room.

        Moves the player into the next room and handles
        whatever consequences have been defined in the
        dungeon.xml file.
        """
        self.location = where
        print "\n", self.location, "\n"

        # Exit if this is the end.
        if self.location.is_exit:
            print "You have won."
            sys.exit(0)

        # Perform monster logic.
        self._manage_monster()

        # Perform Chest Logic
        self._manage_chests()
        
        # Setup available directions menu.
        directions = []
        directions.extend(self.location.exits.keys())
        if self.location.parent:
            directions.append('back')

        while True:
            choice = raw_input("Advance? [%s]: " % ', '.join(directions))
            if choice:
                if choice == 'back' and 'back' in directions:
                    self.advance(self.location.parent)

                try:
                    self.advance(self.location.exits[choice])
                except KeyError:
                    print "That's a brick wall. Try again."
            
class GameHandler(ContentHandler):
    """
    Reads World Definition XML.
    """
    def __init__(self, adventure, *args, **kw):
        ContentHandler.__init__(self, *args, **kw)
        self._stack = []
        self.depth = 0
        self._descr_buf = []
        self.adventure = adventure

    def _get_parent(self):
        parent = None
        if self._stack:
            parent = self._stack[-1]
        return parent
    
    def startElement(self, name, attrs):
        parent = self._get_parent()

        # Handle Structural Objects
        if name in NAV_MAP:
            new_object = NAV_MAP[name](parent)
            if parent:
                parent.add_exit(attrs['direction'], new_object)
            else:
                self.adventure.location = new_object

        # Treasure Chest Contents
        elif name in HP_MAP:
            hp = int(attrs['hp'])
            new_object = HP_MAP[name](hp)
            parent.contents = new_object

        # Monsters!
        elif name == 'monster':
            new_object = Monster(
                attrs['kind'], int(attrs['max_dmg']), int(attrs['min_dmg']))
            parent.monster = new_object

        # Chests themselves.
        elif name == 'chest':
            new_object = Chest()
            parent.chests.append(new_object)

        elif name == 'exit':
            # Set exit attribute on parent.
            parent.is_exit = True
            new_object = Exit()

        # All we have left is descriptions.
        else:
            new_object = Description()

        self._stack.append(new_object)
    def characters(self, content):
        """
        Handles reading chars.

        Responsible for reading in char. data. In our 
        case, we're only dealing with description 
        data.
        """
        if not content.isspace():
            self._descr_buf.append(content.strip())

    def endElement(self, name):
        # This is okay! We're deleting the reference in our
        # stack, not the ones in the data structures
        # we've built. Remember, del simply destroys 
        # a reference and drops the use count.
        del self._stack[-1]

        # If we're closing a documenting tag, then we'll
        # add the string to the parent's desrc field.
        if name == 'description':
            parent = self._get_parent()
            parent.descr = ''.join(self._descr_buf)
            self._descr_buf = []

if __name__ == '__main__':
    a = Adventure('world00.xml')
    a.init_game()
    try:
        a.start_game()
    except YouDiedError, e:
        print str(e)
    except (EOFError, KeyboardInterrupt):
        print "Until next time..."

