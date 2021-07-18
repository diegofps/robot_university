#!/usr/bin/python3

from robotuniversity.python3professor import Python3Professor
from robotuniversity.execution import Execution

template_filepath = "./assets/demo2.template.py"

stud_params = {
    "STUD.IMPORTS": "import math",
    "STUD.FUNCTIONS": "def secret(a,b):\n  return a * b",
    "STUD.SECRET_NAME": "secret"
}

with Python3Professor(template_filepath, stud_params) as prof:

    ex = Execution()
    ex.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ex.expected_stdout = "100\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ex.expected_stdout = "1000\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ex.expected_stdout = "900\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ex.expected_stdout = "1000\n"
    prof.evaluate(ex)
    
    prof.summary().show()
