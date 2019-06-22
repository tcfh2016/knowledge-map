str1 = 'A\u00c4B\U000000e8C'
str2 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for s in str1,str2:
    print('{0}, strlen={1}, '.format(s, len(s)), end='')

    byte1 = s.encode()
    byte2 = s.encode('latin-1')
    #byte3 = s.encode('ascii')
    print('byteslen1={0}, byteslen2={1}'.format(len(byte1), len(byte2)))
