import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', type= str, required= True)
parser.add_argument('--method', type= str, required= False)
parser.add_argument('--columns', type= str, required= False)
parser.add_argument('--columns2', type= str, required= False)
parser.add_argument('--output', type= str, required= False)

args= parser.parse_args()

