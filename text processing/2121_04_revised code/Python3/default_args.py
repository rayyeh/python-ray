from configparser import SafeConfigParser
from optparse import OptionParser

class OptionState(object):
    section = 'cmd_args'
    def __init__(self, defaults='defaults.ini'):
        self.defaults = defaults
        self.parser = SafeConfigParser(
            defaults={
                'server': '127.0.0.1',
                'port': '80',
                'login': ''
            }
        )
        self.parser.read(self.defaults)
        if not self.parser.has_section(self.section):
            self.parser.add_section(self.section)

    def get_option(self, option):
        """
        Return a default argument.
        """
        return self.parser.get(
            self.section, option)

    def set_option(self, option, value):
        """
        Set an option on the parser.

        These can be any element, but we coerce
        them to string to get full interpolation 
        support.
        """
        self.parser.set(
            self.section, option, str(value))

    def store(self, options):
        """
        Serialize out our configuration.
        """
        for op in options.option_list:
            if op.dest:
                self.set_option(
                    op.dest, getattr(opts, op.dest))

        # Write new configuration out.
        with open(self.defaults, 'w') as f:
            self.parser.write(f)

if __name__ == '__main__':
    defs = OptionState()

    options = OptionParser()
    options.add_option('-s', '--server', help="Server Host", default=defs.get_option('server'))
    options.add_option('-p', '--port', help="Server Port", default=defs.get_option('port'))
    options.add_option('-l', '--login', help="Server Login", default=defs.get_option('login'))

    # If this is passed, we'll save our defaults out.
    # Notice this always defaults to False!
    options.add_option('-d', '--save_defaults', help="Save Defaults", action='store_true', default=False)

    opts, args = options.parse_args()

    # Save options
    if opts.save_defaults:
        defs.store(options)
    
    print('login %s:%d as %s' % (opts.server, int(opts.port), opts.login))
