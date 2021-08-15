import argparse
import sys

parser = argparse.ArgumentParser(add_help=False, description=('ArgumentParser example'))
parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument('--numa', '-a', help='number a')
parser.add_argument('--numb', '-b', help='number b')
parser.add_argument('--sum', '-s', help='Caculate sum of a and b')
parser.add_argument('--exit', '-e', help='Quit program')

args = parser.parse_args()

num_a = args.numa
num_b = args.numb

if args.sum:
	print("Sum is ",int(num_a)+int(num_b))
elif args.exit:
	print("exiting")
	exit()
else:
	print(args)
