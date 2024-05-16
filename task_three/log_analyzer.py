def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters logs by the specified logging level.
    
    Arguments:
    logs (list): a list of logs in the form of dictionaries.
    level (str): the logging level to filter.
    
    Returns:
    list: the filtered list of logs.
    """
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of logs for each logging level.
    
    Arguments:
    logs (list): a list of logs as dictionaries.
    
    Returns:
    dict: a dictionary with the number of logs for each level.
    """
    counts = {}
    for log in logs:
        level = log['level']
        if level not in counts:
            counts[level] = 0
        counts[level] += 1
    return counts