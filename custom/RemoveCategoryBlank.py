# # LiteralSymbolSpacer.py
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

import re

from AbstractCustomFormatter import AbstractCustomFormatter


class RemoveCategoryBlank(AbstractCustomFormatter):
    def format_lines(self, lines):
        full = ''.join(lines)
        rst = re.sub(r'@interface [a-zA-Z0-9_]+ \(', self.remove_blank, full)
        # print(rst)

        return rst

    def remove_blank(self, m):
        text = m.group()
        return re.sub(r' +\(', "(", text)


if __name__ == "__main__":
    RemoveCategoryBlank().run()
