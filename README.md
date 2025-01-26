[![Python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org)
[![Tests](https://github.com/freitasgst/caesar-cipher/workflows/Tests/badge.svg)](https://github.com/feitasgst/caesar-cipher/actions)
# Caesar Cipher Encoder
Encode encrypted messages with Caesar Cipher

## Requirements
- Make
- Python 3.12
- Pip >= 21.0.1
- Other requirements: 
    - requirements.txt 
    - requirements-dev.txt (development dependencies)

## Usage
```
make install
```
"Caesar Cipher" technique is one of the most famous substitution ciphers there is.

The **Caesar Cipher Encoder**: 
1. Asks for the rotation number;
2. Asks the user to input the message the user wish to encrypt;
3. The expected **output** is the decrypted message. 

## Contributing

### Installing dev environment requirements:
```
make install-dev
```

### Testing
```
make coverage
```
