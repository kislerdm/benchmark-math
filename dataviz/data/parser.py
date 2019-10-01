import os
import sys
import re
import json
from typing import List, Tuple
import numpy as np


PATH_RESULTS = os.path.join(os.getcwd(), "../../benchmark/results")
PATH_OUTPUT = os.getcwd()
OPERATIONS = ["Multiplication by 2", "Sum",
              "Power of 2", "Sigmoid", "Tanh"]
LANGUAGES = ["cpp", "go", "nodejs",
             "py_vanila", "py_numpy", "r"]
UNIT = 'ms'
FILE_SUFF = ".txt"


def parser(string: str, token: str) -> List[float]:
    """Function to parse string 

      Args:
        string: string to parse
        token: token to use to parse the string

      Returns:
        list
    """
    search_token = re.compile(r"{token}: (.*?){unit}".format(token=token,
                                                             unit=UNIT))
    output = re.findall(search_token, string)
    if len(output) == 0:
        return []

    return [float(i) for i in output]


def box_plot_data(arr: List[float]) -> List[float]:
    """Prepare the list of floats for boxplot: min, q1, q2, q3, q4, q5, max"""
    return list(np.quantile(arr, [0, .25, .5, .5, .75, 1.]))


def median_table(obj: dict) -> Tuple[str]:
    """md table with median values"""
    try:
        columns = list(obj.values())[0].keys()
        header = "| |{}".format(''.join([f"{i}|" for i in columns]))
        alignment = f"""|:---|{''.join(['---:|']*len(columns))}"""
        header = f"{header}\n{alignment}"
        
        rows = []
        for k, v in obj.items():
            cell_1 = f'|{k}|'
            row_values = ''.join([f"{round(i[2], 2)}|" for i in  v.values()])
            row = f"{cell_1}{row_values}"
            rows.append(row)
            
        table = "{}\n{}".format(header, '\n'.join(rows))
        return table, None
    
    except Exception as e:
        return None, e


if __name__ == "__main__":
    assert os.path.isdir(PATH_RESULTS), \
        f"Results path {PATH_RESULTS} doesn't exist"

    files = [i for i in LANGUAGES if i in [
        i.split(FILE_SUFF)[:-1][0] for i in os.listdir(PATH_RESULTS) if i.endswith(FILE_SUFF)]]

    if len(files) == 0:
        print(f"No files found in {PATH_RESULTS}")
        sys.exit(0)

    inpt = {}

    for file in files:
        try:
            with open(os.path.join(PATH_RESULTS, f"{file}{FILE_SUFF}"), 'r') as f:
                data = f.read()

        except Exception as e:
            print(f"Cannot read {file}. Error:\n{e}")
            continue

        inpt[file] = {operation: box_plot_data(parser(data, operation)) for operation in OPERATIONS}

    output = {operation: {file: inpt[file][operation] for file in inpt.keys() if operation in inpt[file].keys()}
              for operation in OPERATIONS}
    
    table, err = median_table(output)
    if err:
        print(err)

    with open(os.path.join(PATH_OUTPUT, "data.json"), 'w') as f:
        json.dump(output, f)

    with open(os.path.join(PATH_OUTPUT, "table.md"), 'w') as f:
        f.write(table)