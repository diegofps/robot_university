from .baseprofessor import BaseProfessor

class Python3Professor(BaseProfessor):

    def __init__(self, exercise):
        if exercise.image_name is None:
            exercise.image_name = "python3image:v0"
        super().__init__("Python3Professor", exercise)
    
    def evaluate(self, ch):

        # Copy and render the template files into the container
        self.deploy(ch)

        # Execute the exercise with current execution parameters
        ch.returncode, ch.stdout, ch.stderr = self.execute("python3 " + self.exercise.mainfile + " " + ch.input_params)

        # Calculate the response correctness
        if ch.returncode != ch.expected_returncode:
            ch.issues_explanation.append("returncode is not correct")

        if not self.soft_compare(ch.stdout, ch.expected_stdout):
            ch.issues_explanation.append("stdout is not correct")
        
        if not self.soft_compare(ch.stderr, ch.expected_stderr):
            ch.issues_explanation.append("stderr is not correct")
        
        ch.correctness = 0.0 if ch.issues_explanation else 1.0

        # Add respose to summary
        self.add_challenge(ch)
