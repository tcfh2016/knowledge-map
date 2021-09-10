test_lines = [
'1st test line ',
'2nd test line\n',
'3rd test line  \n'
]

striped_lines = map(lambda x: x.replace(' ', ''), test_lines)
print(test_lines)
print(list(striped_lines))
