#!/usr/bin/python3

from robotuniversity.python3professor import Python3Professor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.templates.append( ("./classes/python3/exercise1/main.template.py", "/app/exercise1.py") )
exercise.mainfile = "/app/exercise1.py"
exercise.stud_params = {
    "STUD.IMPORTS": "import math",
    "STUD.FUNCTIONS": "def secret(a,b):\n  return a * b",
    "STUD.SECRET_NAME": "secret"
}

with Python3Professor(exercise) as prof:

    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.evaluate(ch)
    
    prof.summary().show()
