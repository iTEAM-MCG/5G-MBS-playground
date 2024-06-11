import configparser

class UtilsConfigParser(configparser.ConfigParser):
    """
    Patched ConfigParser class that removes double quotes from values
    """

    def get(self, section, option, *, raw=False, vars=None, fallback=configparser._UNSET):
        """Overriden get() method to remove the double quotes from values"""
        value = super().get(section, option, raw=raw, vars=vars, fallback=fallback)
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        return value
