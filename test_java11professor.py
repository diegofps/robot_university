#!/usr/bin/python3

from robotuniversity.java11professor import Java11Professor
from robotuniversity.challenge import Challenge
from robotuniversity.exercise import Exercise

exercise = Exercise()
exercise.add_asset(local_filepath="./classes/java11/exercise1/Main.mf", env_filepath="/Main.mf")
exercise.add_template(local_filepath="./classes/java11/exercise1/src/Main.template.java", env_filepath="/src/Main.java")
exercise.mainfile = "/main.jar"
exercise.stud_params = {
    "STUD.IMPORTS": "",
    "STUD.FUNCTIONS": "public static int secret(int a, int b) {\n        return a * b;\n    }",
    "STUD.SECRET_NAME": "secret"
}

with Java11Professor(exercise) as prof:

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
