import re

__all__ = ('pre_format_dict')

def format_dict_trail(m):
    text = m.group()
    # Unformatted comment statements
    if text.find('//') >= 0:
        return text
    return re.sub(r',\s*}', "}", text)

def pre_format_dict(full_text):
    # optimized nesting dict
    rst = re.sub(r': +@{\n+\s+', ": @{", full_text)
    
    # remove '\n' at leading of @{}
    # rst = re.sub(r'@{\n+ +', "@{", rst)

    # remove trail ',' at end of @{}
    rst = re.sub(r'.*: *[a-zA-Z0-9_@,}\s\.\(\)\[\]]+,\s*}]?[;\n]', format_dict_trail, rst)
    return rst
