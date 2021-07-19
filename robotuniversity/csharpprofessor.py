from .baseprofessor import BaseProfessor
from .compilation import Compilation

class CSharpProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "monoimage:v0"
    
    super().__init__("CSharpProfessor", exercise)
  
  def compile(self, exercise, challenge):
    sources = [x[1] for x in exercise.templates if x[1].endswith(".cs")]
    sources += [x[1] for x in exercise.assets if x[1].endswith(".cs")]
    cmd = "mcs " + "".join(sources) + " -out:" + exercise.mainfile
    
    comp = Compilation()
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0

    challenge.compilation = comp

  def add_challenge(self, ch):

    # Copy and render the template files into the container, compile if necessary
    self.deploy(ch)

    # Execute the exercise with current execution parameters
    ch.returncode, ch.stdout, ch.stderr = self.execute("mono " + self.exercise.mainfile + " " + ch.input_params)

    # Add respose to summary
    self.add_challenge_result(ch)
