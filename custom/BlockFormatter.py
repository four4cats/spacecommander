# # LiteralSymbolSpacer.py
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

import sys
import os
import re

from AbstractCustomFormatter import AbstractCustomFormatter

class BlockFormatter(AbstractCustomFormatter):
    def format_lines(self, lines):
        full = ''.join(lines)
        # format ' ' between '){'
        rst = re.sub(r'\) *{', ') {', full)
        # print(rst)

        return rst

if __name__ == "__main__":
    BlockFormatter().run()
