import pandas as pd

def print_head(df):
    print(df.head())

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="Task to run. Must be name of a function in this object.", type=str, required=True)
    parser.add_argument("--input", help="Path to accounting file. Must be readable by user.", type=str, required=True)
    args = parser.parse_args()
    schema = None
    input_df = pd.read_csv(args.input, sep=":", names=schema)
    parser.task(input_df)