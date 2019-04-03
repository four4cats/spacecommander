# # LiteralSymbolSpacer.py
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

import sys
import os
import re

from AbstractCustomFormatter import AbstractCustomFormatter

class DictFormatter(AbstractCustomFormatter):
    def format_lines(self, lines):
        full = ''.join(lines)
        # Remove the blanks at the beginning of the dict
        full = re.sub(r'@{\s*\n*\s*', "@{", full)
        sentence = r'(?:@?[\(\["]?[a-zA-Z0-9_\s]*[\)\]"]?)'
        rex = '.*@{\s*(?:%s:\s*%s,?\s*)*}' % (sentence, sentence)
        print(rex)
        rst = re.sub(rex, self.format_dict, full)
        # print(rst)

        return rst

    def format_dict(self, m):

        rst = m.group()
        # Remove the blanks at the end of the dict
        rst = re.sub(r',?\s+}', '}', rst)
        if rst.endswith(' }'):
            rst = rst[:-2] + '}'

        lines = rst.split('\n')
        if len(lines) == 1:
            return rst

        rst_lines = []
        rst_lines.append(lines[0])

        # Align Parameters
        begin_index = lines[0].find('{') + 2
        white_space = ' '.join(['' for x in range(0, begin_index)])
        for x in range(1, len(lines)):
            line = lines[x]
            a_line = white_space + line.lstrip()
            rst_lines.append(a_line)

        return '\n'.join(rst_lines)

if __name__ == "__main__":
    # path = os.path.abspath(sys.argv[0])
    # path = os.path.split(path)[0]
    # src_path = os.path.abspath(os.path.join(path, '..', 'Testing Support', 'TestDict.m'))
    # sys.argv.append(src_path)
    DictFormatter().run()
