import json
from typing import List
import ast

import pandas as pd

from data.common.schemas import Chart
from data.common.utils import convert_json_to_chart_objects


def find_label_index_in_prompt(label: str, prompt: str) -> int:
    """
    find index of a word in prompt if it is present there
    """
    label = label.lower()
    prompt = prompt.lower()

    l, r = 0, 0

    while l < len(prompt):
        r = l
        label_i = 0

        while prompt[r:r+1] == label[label_i:label_i+1]:
            r += 1
            label_i += 1

            if label_i == len(label):
                return l

        l += 1

    return -1


def find_value_index_in_prompt(value: str, prompt: str) -> int:
    """
    find index of a value in prompt if it is present there
    """
    value = value.lower()
    prompt = prompt.lower()

    l, r = 0, 0

    while l < len(prompt):
        r = l
        curr_digit = ""

        while True:
            if r == len(prompt):
                break

            if prompt[r:r+1] in [",", ", ", ".", ". "] and len(curr_digit) > 0:
                r += 1
                continue

            if prompt[r:r+1].isdigit():
                curr_digit += prompt[r:r+1]
                r += 1
                continue

            break

        if curr_digit and curr_digit == value:
            return l

        if curr_digit:
            l = r + 1
            continue

        l += 1

    return -1


def validate_single_item(chart: Chart, prompt: str) -> bool:
    """
    validates a single chart
    """
    labels_indexes = [float("-inf")]
    values_indexes = [float("-inf")]

    for label in chart.data:
        label_index = find_label_index_in_prompt(label=label.label, prompt=prompt)
        if label_index == -1:
            return False
        if label_index < labels_indexes[-1]:
            return False

        value_index = find_value_index_in_prompt(value=str(label.value), prompt=prompt)
        if value_index == -1:
            return False
        if value_index < values_indexes[-1]:
            return False

        labels_indexes.append(label_index)
        values_indexes.append(value_index)

    return True


def validate(chart_jsons: List[dict], prompts: List[str]) -> List[bool]:
    charts = convert_json_to_chart_objects(chart_jsons=chart_jsons)

    c = 0
    validation_bools = []

    for i, chart in enumerate(charts):
        is_valid = validate_single_item(chart=chart, prompt=prompts[i])
        if is_valid:
            c += 1

        validation_bools.append(is_valid)

    print("Number of valid LLM prompts: ", c)

    return validation_bools


def main():
    """
    adds column about validity of LLM generated prompt
    """
    df = pd.read_csv("final.csv")
    chart_jsons = [ast.literal_eval(chart_json) for chart_json in df["Data in JSON"]]
    validation_bools = validate(chart_jsons=chart_jsons, prompts=df["LLM Generated"])
    df["LLM generated prompt is valid"] = validation_bools
    df.to_csv("final_validated.csv", index=False)


if __name__ == "__main__":
    main()
