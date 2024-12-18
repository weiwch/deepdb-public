import os
import subprocess

def count_lines_in_file(file_path):
    """
    Count the number of lines in a file using wc -l command.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: Number of lines in the file.
    """
    try:
        output = subprocess.check_output(f"wc -l {file_path}", shell=True)
        lines = int(output.split()[0])
        return lines
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None

def main():
    # folder_path = input("Enter the folder path: ")
    # folder_path = "../data/tpch100/workload/static/data"
    folder_path = "../data/STATS/workload/dist_shift/data"
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    print(files)
    
    # Count the number of lines in each file
    lim = 1001
    leq_lim = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        lines = count_lines_in_file(file_path)
        if lines is not None:
            print(f"File: {file}, Lines: {lines}")
        if lines >= lim:
            leq_lim.append(file)
    leq_lim.sort()
    for x in leq_lim:
        print("'{}'".format(x), end=" ")
    
if __name__ == "__main__":
    main()