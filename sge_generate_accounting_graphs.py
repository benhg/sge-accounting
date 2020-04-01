import pandas as pd

def print_head(df):
    print(df.head())

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="Task to run. Must be name of a function in this object.", type=str, required=True)
    parser.add_argument("--input", help="Path to accounting file. Must be readable by user.", type=str, required=True)
    args = parser.parse_args()
    schema = ["qname", "hostname", "group", "owner", "job_name", "job_number", "account", "priority", "submission_time", "start_time", "end_time", "failed", "exit_status", "ru_wallclock", "project", "department", "granted_pe", "slots", "task_number", "cpu", "mem", "io", "category", "iow", "pe_taskid", "maxvmem", "arid", "ar_submission_time"]
    input_df = pd.read_csv(args.input, sep=":", names=schema, skiprows=4)
    eval(args.task)(input_df)