#!/usr/bin/python3

from robotuniversity.cppprofessor import CPPProfessor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.templates.append( ("./classes/cpp/exercise1/main.template.cpp", "/app/main.cpp") )
exercise.mainfile = "/app/main"
exercise.stud_params = {
    "STUD.IMPORTS": "",
    "STUD.FUNCTIONS": "int secret(int const a, int const b) {\n        return a * b;\n    }",
    "STUD.SECRET_NAME": "secret"
}

with CPPProfessor(exercise) as prof:

    ch = Challenge()
    ch.input_params = "10 10"
    ch.expected_stdout = "100"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.input_params = "50 20"
    ch.expected_stdout = "1000"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.input_params = "10 90"
    ch.expected_stdout = "900"
    prof.evaluate(ch)
    
    ch = Challenge()
    ch.input_params = "-10 -100"
    ch.expected_stdout = "1000"
    prof.evaluate(ch)
    
    prof.summary().show()
