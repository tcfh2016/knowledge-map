bytes_literal = b'Copyright \xc2\xa9'
print('bytes_literal = ', bytes_literal)
print('bytes_literal.decode() = ', bytes_literal.decode())
print('bytes_literal.decode(utf-8) = ', bytes_literal.decode('utf-8'))
print('bytes_literal.decode(utf-16) = ', bytes_literal.decode('utf-16'))

str_literal = 'Trademark ©'
bytes_encoded = str_literal.encode()
print('bytes_encoded = ', bytes_encoded)
print('bytes_encoded.decode() = ', bytes_encoded.decode())
print('bytes(str_literal) ->', bytes(str_literal, 'utf-8'))
