from .baseprofessor import BaseProfessor
from .compilation import Compilation

class CProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "clangimage:v0"
    
    super().__init__("CProfessor", exercise)
  
  def compile(self, exercise, challenge):
    sources = [x[1] for x in exercise.templates if x[1].endswith(".c")]
    sources += [x[1] for x in exercise.assets if x[1].endswith(".c")]

    cmd = "clang " + "".join(sources) + " -o " + challenge.rootpath + exercise.mainfile
    
    comp = Compilation()
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0

    challenge.compilation = comp
