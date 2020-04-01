import pandas as pd
import numpy as np
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

def task_lengths_hist(df, save_figure):
    lengths = df.ru_wallclock
    bins = np.linspace(0, 40000, 100)
    plt.hist(lengths, bins=bins, log=True)
    plt.title("Histogram of BLT Job Run Times (Seconds)")
    plt.ylabel("Frequency (Log scale)")
    plt.xlabel("Run time (sec). [Truncated]")
    if not save_figure:
        plt.show()
    else:
        plt.savefig("somefig.png")

def tasks_by_type(df, save_figure):
    tasks_per_type = df.category.value_counts()
    vals = list(tasks_per_type.values)[:20]
    labels = list(tasks_per_type.index)[:20]
    plt.title("Number of tasks by job type")
    plt.bar( labels, vals,)

    if not save_figure:
        plt.show()
    else:
        plt.savefig("somefig.png")

def tasks_by_host(df, save_figure):
    tasks_per_host = df.hostname.value_counts()
    vals = list(tasks_per_host.values)[:20]
    labels = list(tasks_per_host.index)[:20]
    plt.title("Number of tasks by Host type")
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