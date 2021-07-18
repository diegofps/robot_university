from .baseprofessor import BaseProfessor

class Python3Professor(BaseProfessor):

    def __init__(self, template_filepath, stud_params, image_name="python3image:v0"):
        super().__init__("Python3Professor", template_filepath, stud_params, image_name)
    
    def compile(self, _):
        print("You don't need to call compile on a python app")

    def evaluate(self, ex):
        # Create the program inside the container, run it and capture its outputs
        ex.prof_program = self.render(self.stud_program, ex.prof_params)
        self.create_file("/app/main.py", ex.prof_program, True)
        ex.returncode, ex.stdout, ex.stderr = self.execute("/app/main.py " + ex.input_params)

        # Calculate the response correctness
        if ex.returncode != ex.expected_returncode:
            ex.issues_explanation.append("returncode is not correct")

        if not self.soft_compare(ex.stdout, ex.expected_stdout):
            ex.issues_explanation.append("stdout is not correct")
        
        if not self.soft_compare(ex.stderr, ex.expected_stderr):
            ex.issues_explanation.append("stderr is not correct")
        
        ex.correctness = 0.0 if ex.issues_explanation else 1.0

        # Add respose to summary
        self.add_execution(ex)
