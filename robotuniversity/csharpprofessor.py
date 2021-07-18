from .baseprofessor import BaseProfessor
from .compilation import Compilation

class CSharpProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "monoimage:v0"
    super().__init__("CSharpProfessor", exercise)
  
  def compile(self, exercise, challenge):
    comp = Compilation()
    sources = "".join([x[1] for x in exercise.templates if x[1].endswith(".cs")])
    sources += "".join([x[1] for x in exercise.assets if x[1].endswith(".cs")])
    cmd = "mcs " + sources + " -out:" + exercise.mainfile
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0
    challenge.compilation = comp

  def evaluate(self, ch):

    # Copy and render the template files into the container, compile if necessary
    self.deploy(ch)

    # Execute the exercise with current execution parameters
    ch.returncode, ch.stdout, ch.stderr = self.execute("mono " + self.exercise.mainfile + " " + ch.input_params)

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
