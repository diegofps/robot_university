class Challenge:

    def __init__(self):
        
        self.idd = -1
        self.rootpath = "/"

        self.expected_returncode = 0
        self.expected_stdout = ""
        self.expected_stderr = ""

        self.input_params = ""
        self.prof_program = ""
        self.prof_params = {}
        
        self.returncode = 0
        self.stdout = ""
        self.stderr = ""

        self.issues_explanation = []
        self.correctness = 0.0
        self.compilation = None

    def show(self, indentation, include_program=False):
        prefix = " " * indentation

        print()
        print(prefix + "Challenge %d:" % self.idd)
        print(prefix + "  env_rootpath: " + str(self.rootpath))
        print(prefix + "  input_params: " + self.input_params)
        print(prefix + "  prof_params: " + str(self.prof_params))

        if include_program:
            print(prefix + "  prof_program: " + self.prof_program)
        
        print()
        print(prefix + "  Expected: ")
        print(prefix + "    returncode: " + str(self.expected_returncode))
        print(prefix + "    stdout: " + self.expected_stdout)
        print(prefix + "    stderr: " + self.expected_stderr)

        print()
        print(prefix + "  Obtained: ")
        print(prefix + "    returncode: " + str(self.returncode))
        print(prefix + "    stdout: " + self.stdout)
        print(prefix + "    stderr: " + self.stderr)

        print(prefix + "    issues_explanation: " + str(self.issues_explanation))
        print(prefix + "    correctness: " + str(self.correctness))

        if self.compilation:
            self.compilation.show(indentation + 2, include_program)
        