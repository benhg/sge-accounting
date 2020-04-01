import pandas as pd
import matplotlib.pyplot as plt

def print_head(df, save_figure):
    print(df.head())

def tasks_by_user(df, save_figure):
    tasks_per_user = df.owner.value_counts()
    vals = list(tasks_per_user.values)[:20]
    labels = list(tasks_per_user.index)[:20]
    plt.title("Top 20 users by number of BLT jobs run")
    plt.bar( labels, vals,)

    if not save_figure:
        plt.show()
    else:
        plt.savefig("somefig.png")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="Task to run. Must be name of a function in this object.", type=str, required=True)
    parser.add_argument("--input", help="Path to accounting file. Must be readable by user.", type=str, required=True)
    parser.add_argument("--save_figure", help="If this is specified, save figure instead of showing plot", action="store_true")
    args = parser.parse_args()
    schema = ["qname", "hostname", "group", "owner", "job_name", "job_number", "account", "priority", "submission_time", "start_time", "end_time", "failed", "exit_status", "ru_wallclock","ru_utime", "ru_stime", "ru_maxrss","ru_ixrss","ru_ismrss", "ru_idrss", "ru_isrss", "ru_minflt", "ru_majflt", "ru_nswap", "ru_inblock", "ru_oublock", "ru_msgsnd", "ru_msgrcv", "ru_nsignals", "ru_nvcsw", "ru_nivcsw", "project", "department", "granted_pe", "slots", "task_number", "cpu", "mem", "io", "category", "iow", "pe_taskid", "maxvmem", "arid", "ar_submission_time"]
    input_df = pd.read_csv(args.input, sep=":", names=schema, skiprows=4)
    eval(args.task)(input_df, args.save_figure)