from .baseprofessor import BaseProfessor
from .compilation import Compilation
import os

class CProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "clangimage:v0"
    
    super().__init__("CProfessor", exercise)
  
  def compile(self, exercise, challenge):
    sources = [challenge.rootpath + x.env_filepath for x in exercise.templates if x.env_filepath.endswith(".c")]
    sources += [challenge.rootpath + x.env_filepath for x in exercise.assets if x.env_filepath.endswith(".c")]
    
    output_filepath = challenge.rootpath + exercise.mainfile
    output_folderpath = os.path.dirname(output_filepath)

    self.create_folder(output_folderpath)

    cmd = "clang " + " ".join(sources) + " -o " + output_filepath
    
    comp = Compilation()
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0

    challenge.compilation = comp
