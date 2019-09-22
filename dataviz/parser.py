import os
import sys
import re
import json
from typing import List
import numpy as np


PATH_RESULTS = os.path.join(os.getcwd(), "../benchmark/results")
PATH_OUTPUT = os.path.join(os.getcwd(), "data.json")
OPERATIONS = ["Multiplication by 2", "Sum",
              "Power of 2", "Sigmoid", "Tanh"]
UNIT = 'ms'


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


if __name__ == "__main__":
    assert os.path.isdir(PATH_RESULTS), \
        f"Results path {PATH_RESULTS} doesn't exist"

    files = [i for i in os.listdir(PATH_RESULTS) if i.endswith('.txt')]

    if len(files) == 0:
        print(f"No files found in {PATH_RESULTS}")
        sys.exit(0)

    output = {}
    
    for file in files:
        with open(os.path.join(PATH_RESULTS, file), 'r') as f:
            data = f.read()

        key = ''.join(file.split('.txt')[:-1])

        output[key] = {operation: box_plot_data(parser(data, operation))
                       for operation in OPERATIONS}

    with open(PATH_OUTPUT, 'w') as f:
      json.dump(output, f)
