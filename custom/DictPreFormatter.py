# # LiteralSymbolSpacer.py
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

import re

from AbstractCustomFormatter import AbstractCustomFormatter

class DictPreFormatter(AbstractCustomFormatter):
    def format_lines(self, lines):
        full = ''.join(lines)
        rst = re.sub(r': +@{\n+ +', ": @{", full)
        rst = re.sub(r',\n+ +},', "},", rst)
        rst = re.sub(r'.*: [a-zA-Z0-9_@,}\s\.\(\)]*,\s+}[;\n]', self.format_dict_trail, rst)
        # print(rst)

        return rst

    def format_dict_trail(self, m):
        text = m.group()
        if text.find('//') >= 0:
          return text
        return re.sub(r',?\n +}', "}", text)


if __name__ == "__main__":
    DictPreFormatter().run()
