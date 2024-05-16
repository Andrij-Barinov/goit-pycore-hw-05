def display_log_counts(counts: dict):
    """
    Formats and displays the results of counting logs by level.
    
    Arguments:
    counts (dict): a dictionary with the number of logs for each level.
    """
    print("Logging level | Quantity")
    print("--------------|---------")
    for level, count in counts.items():
        print(f"{level.ljust(13)} | {count}")