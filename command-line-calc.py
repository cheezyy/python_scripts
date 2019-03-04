'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

import argparse
import sys

'''
Run from command line:
python command-line-calc [-h] [--x X] [--y Y] [--operation OPERATION]

Where:    -h = help
        --x = arg1 (float)
        --y = arg2 (float)
--operation = calculation type (add, sub, mul, div)
(All optional, default is 1+1)
'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='Enter first number')
    parser.add_argument('--y', type=float, default=1.0, help='Enter second number')
    parser.add_argument('--operation', type=str, default='add', help='Enter operation [add, sub, mul, div]')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()