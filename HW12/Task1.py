"""
In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.

1. Create a script with arguments:

exp; required: false; default: min(exp)
current_job_exp; required: false; default: max(current_job_exp)
sex; required: false
city; required: false
position; required: false
age; required: false
path_to_source_files; required: true;
destination_path; required: false; default: .
destination_filename; required: false; default: f"2020_june_mini.csv".
The script should read the .csv file and get the information based on your input and generate a new .csv
file with that info

Example of input:
-exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...
"""
import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('--exp', required=False, default='min(exp)')
parser.add_argument('--current_job_exp',  required=False, default='max(current_job_exp)')
parser.add_argument('--sex', required=False)
parser.add_argument('--city', required=False)
parser.add_argument('--position', required=False)
parser.add_argument('--age', required=False)
parser.add_argument('--path_to_source_files', required=True)
parser.add_argument('--destination_path', required=False, default='')
parser.add_argument('--destination_filename', required=False, default=f"new_2020_june_mini.csv")


args = parser.parse_args()


path = args.path_to_source_files
des_path = args.destination_path + args.destination_filename


lis = []
with open(path, encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    head = reader.fieldnames
    for row in reader:
        if (
                row['exp'] == args.exp
                and row['Город'] == args.city
                and row['Пол'] == args.sex
                and row['Должность'] == args.position
        ):

            lis.append([row["N"],
                        row["Город"],
                        row["Зарплата.в.месяц"],
                        row["Изменение.зарплаты.за.12.месяцев"],
                        row["Должность"],
                        row["exp"],
                        row["current_job_exp"],
                        row["Язык.программирования"],
                        row["Специализация"],
                        row["Возраст"],
                        row["Пол"],
                        row["Образование"],
                        row["Университет"],
                        row["Еще.студент"],
                        row["Уровень.английского"],
                        row["Размер.компании"],
                        row["Тип.компании"],
                        row["Предметная.область"]])


with open(des_path, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=head)
    writer.writeheader()
    writer = csv.writer(csv_file)
    for el in lis:
        writer.writerow(el)

# input
# --exp 3 --sex female --position DevOps --city Kyiv --path 2020_june_mini.csv
