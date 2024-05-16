import sys

def parse_log_line(line: str) -> dict:
    """
    Parses a line of a log file and returns a dictionary with components.
    
    Arguments:
    line (str): the log line.
    
    Returns:
    dict: a dictionary with date, time, logging level, and message.
    """
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """
    Loads logs from a file and returns a list of dictionaries with log components.
    
    Arguments:
    file_path (str): the path to the log file.
    
    Returns:
    list: a list of logs in the form of dictionaries.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)
    return logs