"""
2. Create a script with arguments:

source_file_path; required: true;
start_salary; required: false; help: starting point of salary;
end_salary; required: false; help: the max point of salary;
position; required: false; help: position role
age; required: false; help: Age of person
language; required: false; help; Programming language

Based on this info generate a new report of average salary.
"""

import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('--source_file_path', required=True)
parser.add_argument('--start_salary', required=False, help='starting point of salary')
parser.add_argument('--end_salary', required=False, help='the max point of salary')
parser.add_argument('--position', required=False, help='position role')
parser.add_argument('--age', required=False, help='Age of person')
parser.add_argument('--language', required=False, help='Programming language')

args = parser.parse_args()


count = 0
average_salary = 0
with open(args.source_file_path, encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        if (
                float(args.end_salary) > float(row['Зарплата.в.месяц']) > float(args.start_salary)
                and row['Должность'] == args.position
                and row['Возраст'] == args.age
                and row['Язык.программирования'] == args.language
        ):

            count += 1
            average_salary += float(row['Зарплата.в.месяц'])


print(f'Average salary: {average_salary/count}')

# input
#  --source_file_path 2020_june_mini.csv --start_salary 0 --end_salary 18000 --position "Team/Technical Lead"
#  --age 28 --language Python








        

