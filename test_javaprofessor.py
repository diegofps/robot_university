#!/usr/bin/python3

from robotuniversity.javaprofessor import JavaProfessor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.add_template(local_filepath="./classes/java/exercise1/main.template.java", env_filepath="/app/main.java")
exercise.mainfile = "/app/main.jar"
exercise.stud_params = {
    "STUD.IMPORTS": "",
    "STUD.FUNCTIONS": "public static int secret(int const a, int const b) {\n        return a * b;\n    }",
    "STUD.SECRET_NAME": "secret"
}

with JavaProfessor(exercise) as prof:

    ch = Challenge()
    ch.input_params = "10 10"
    ch.expected_stdout = "100"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.input_params = "50 20"
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.input_params = "10 90"
    ch.expected_stdout = "900"
    prof.add_challenge(ch)
    
    ch = Challenge()
    ch.input_params = "-10 -100"
    ch.expected_stdout = "1000"
    prof.add_challenge(ch)
    
    prof.summary().show()
