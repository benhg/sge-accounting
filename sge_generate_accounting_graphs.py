import pandas as pd


if __name__ == '__main__':
	import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", help="Graph to generate. Must be name of a function in this object.", type=str, required=True)
    parser.add_argument("--input", help="Path to accounting file. Must be readable by user.", type=str, required=True)
    args = parser.parse_args()
    