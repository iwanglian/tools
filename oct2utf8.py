#!/usr/bin/env python
# -*- coding: utf-8 -*-

def unescape(s):
    result = ""
    while len(s) > 0:
        if s[0] == "\\":
            (octbyte, s) = (s[1:4], s[4:])
            try:
                result += chr(int(octbyte, 8))
            except ValueError:
                result += "\\"
                s = octbyte + s
        else:
            result += s[0]
            s = s[1:]
    return result

if __name__ == '__main__':
	oct_str = r"\242\206\336\311\377\000\t\027\314k\203\251J\343z\335\340\343\267H\243\310\235D\257\363S\351:\221>\347\232\367\2357"
	print unescape(oct_str).decode('gb2312') 
