#!/usr/bin/python3

from robotuniversity.csharpprofessor import CSharpProfessor
from robotuniversity.execution import Execution

template_filepath = "./classes/mono/exercise1.template.cs"

stud_params = {
    "STUD.IMPORTS": "",
    "STUD.FUNCTIONS": "public static int secret(int a, int b) {\n        return a * b;\n    }",
    "STUD.SECRET_NAME": "secret"
}

with CSharpProfessor(template_filepath, stud_params) as prof:

    ex = Execution()
    ex.input_params = "10 10"
    ex.expected_stdout = "100\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = "50 20"
    ex.expected_stdout = "1000\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = "10 90"
    ex.expected_stdout = "900\n"
    prof.evaluate(ex)
    
    ex = Execution()
    ex.prof_params = "-10 -100"
    ex.expected_stdout = "1000\n"
    prof.evaluate(ex)
    
    prof.summary().show()
