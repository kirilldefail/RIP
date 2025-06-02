import json
import sys
import re
import random
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.sort import sort
from lab_python_fp.get_random import get_random

path = '/Users/nonpenguin/my/pythonchic/rip/my_labs/lab3/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, "job-name"), ignore_case=True)))

@print_result
def f2(arg):
    r = re.compile("программист*|Программист*")
    return list(filter(r.match, arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salary =list(map(lambda str: " с зарплатой {} рублей".format(str), get_random(len(arg), 100000, 200000)))
    arg_with_salary = list(zip(arg, salary))
    return list(map(lambda str: "{}{}".format(str[0], str[1]), arg_with_salary))

if __name__ == '__main__':
    with cm_timer_1():
       f4(f3(f2(f1(data))))
