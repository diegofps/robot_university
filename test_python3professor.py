#!/usr/bin/python3

from robotuniversity.python3professor import Python3Professor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.add_template(local_filepath="./classes/python3/exercise1/main.template.py", env_filepath="exercise1.py")
exercise.mainfile = "exercise1.py"
exercise.stud_params = {
    "STUD.IMPORTS": "import math",
    "STUD.FUNCTIONS": "def secret(a,b):\n  return a * b",
    "STUD.SECRET_NAME": "secret"
}

with Python3Professor(exercise) as prof:

    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "10"}
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "50", 'PROF.P2': "20"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "10", 'PROF.P2': "90"}
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.prof_params = {'PROF.P1': "-10", 'PROF.P2': "-100"}
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    prof.summary().show()
