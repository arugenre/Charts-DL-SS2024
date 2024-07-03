import json
import random
from itertools import cycle

from data.common.utils import shuffle_data

COMPLEXITY_MIN = 13
COMPLEXITY_MAX = 13
QUANTITY_PER_COMPLEXITY = 50


CATEGORY_PROBLEMS_TITLE_SAMPLES = [
    "Number of problems across different categories in Leetcode",
    "Problem distribution by category in Leetcode",
    "Tally of problems per category on Leetcode",
    "Leetcode problem count by category",
    "Count of issues across Leetcode categories",
    "Breakdown of problems by category in Leetcode",
    "Categories of problems and their counts on Leetcode",
    "Leetcode's problem categories and their counts",
    "Total problems per category in Leetcode",
    "Category-wise problem count on Leetcode",
    "Leetcode problem statistics by category",
    "Number of issues categorized in Leetcode",
    "Problem counts across Leetcode categories",
    "Leetcode categories and their problem totals",
    "Count of Leetcode problems by category",
    "Distribution of problems across Leetcode categories",
    "Leetcode problem tally by category",
    "Problems in each category on Leetcode",
    "Leetcode problem totals by category",
    "Problem counts by category on Leetcode",
    "Categorized problem counts in Leetcode",
    "Leetcode problem numbers per category",
    "Category-wise tally of problems in Leetcode",
    "Leetcode issues count by category",
    "Problems sorted by category in Leetcode",
    "Count of categorized problems on Leetcode",
    "Leetcode's categorized problem counts",
    "Number of problems in each Leetcode category",
    "Leetcode category-wise problem numbers",
    "Problem count per Leetcode category",
]

COMPANY_PROBLEMS_TITLE_SAMPLES = [
    "Number of problems across different companies in Leetcode",
    "Problem distribution by company in Leetcode",
    "Tally of problems per company on Leetcode",
    "Leetcode problem count by company",
    "Count of issues across Leetcode companies",
    "Breakdown of problems by company in Leetcode",
    "Companies and their problem counts on Leetcode",
    "Leetcode's problem counts by company",
    "Total problems per company in Leetcode",
    "Company-wise problem count on Leetcode",
    "Leetcode problem statistics by company",
    "Number of issues categorized by company in Leetcode",
    "Problem counts across Leetcode companies",
    "Leetcode companies and their problem totals",
    "Count of Leetcode problems by company",
    "Distribution of problems across Leetcode companies",
    "Leetcode problem tally by company",
    "Problems in each company on Leetcode",
    "Leetcode problem totals by company",
    "Problem counts by company on Leetcode",
    "Categorized problem counts in Leetcode by company",
    "Leetcode problem numbers per company",
    "Company-wise tally of problems in Leetcode",
    "Leetcode issues count by company",
    "Problems sorted by company in Leetcode",
    "Count of categorized problems on Leetcode by company",
    "Leetcode's categorized problem counts by company",
    "Number of problems in each Leetcode company",
    "Leetcode company-wise problem numbers",
    "Problem count per Leetcode company",
]


def balance():
    cycled_chart_types = cycle(["bar", "pie"])

    output_data = []

    with open("Leetcode/balanced_output.json", "r") as f:
        output_data = json.loads(f.read())

    category_problems = []
    company_problems = []

    with open("Leetcode/leetcode_categories.json", "r") as f:
        category_problems = json.loads(f.read())

    with open("Leetcode/leetcode_companies.json", "r") as f:
        company_problems = json.loads(f.read())

    for i in range(COMPLEXITY_MIN, COMPLEXITY_MAX + 1):
        for j in range(QUANTITY_PER_COMPLEXITY // 2):

            shuffled_category_problems = shuffle_data(
                labels_length=i,
                full_data=category_problems
            )
            output_data.append({
                "chart_type": next(cycled_chart_types),
                "chart_title": CATEGORY_PROBLEMS_TITLE_SAMPLES[random.randint(0, len(CATEGORY_PROBLEMS_TITLE_SAMPLES)-1)],
                "data": [
                    {
                        "label": problem["label"],
                        "value": problem["value"],
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for problem in shuffled_category_problems
                ]
            })

            shuffled_company_problems = shuffle_data(
                labels_length=i,
                full_data=company_problems
            )
            output_data.append({
                "chart_type": next(cycled_chart_types),
                "chart_title": COMPANY_PROBLEMS_TITLE_SAMPLES[random.randint(0,
                                                                              len(COMPANY_PROBLEMS_TITLE_SAMPLES) - 1)],
                "data": [
                    {
                        "label": problem["label"],
                        "value": problem["value"],
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for problem in shuffled_company_problems
                ]
            })

    with open("Leetcode/balanced_output.json", "w") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    balance()
