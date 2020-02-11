#The Content has been made available for informational and educational purposes only
import argparse
parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
parser.add_argument('-a','--account',required=True)
args = parser.parse_args()
from evolut import evolut
print(evolut(args.account))
