#!/usr/bin/python3

from robotuniversity.csharpprofessor import CSharpProfessor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.templates.append( ("./classes/mono/exercise1/exercise1.template.cs", "/app/exercise1.cs") )
exercise.mainfile = "/app/exercise1.exe"
exercise.stud_params = {
    "STUD.IMPORTS": "",
    "STUD.FUNCTIONS": "public static int secret(int a, int b) {\n        return a * b;\n    }",
    "STUD.SECRET_NAME": "secret"
}

with CSharpProfessor(exercise) as prof:

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
