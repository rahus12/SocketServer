import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='The name of the person')
parser.add_argument('--age', type=int, help='The age of the person')

args = parser.parse_args()

# print(sys.argv[1])
# print(sys.argv[2])

print(args.name)
print(args.age)