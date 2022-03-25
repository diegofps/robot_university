from .baseprofessor import BaseProfessor
from .compilation import Compilation
import os

class CSharpProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "monoimage:v0"
    
    super().__init__("CSharpProfessor", exercise)
  
  def compile(self, exercise, challenge):
    sources = [challenge.rootpath + x.env_filepath for x in exercise.templates if x.env_filepath.endswith(".cs")]
    sources += [challenge.rootpath + x.env_filepath for x in exercise.assets if x.env_filepath.endswith(".cs")]

    output_filepath = challenge.rootpath + exercise.mainfile
    output_folderpath = os.path.dirname(output_filepath)

    self.create_folder(output_folderpath)
    
    cmd = "mcs " + " ".join(sources) + " -out:" + output_filepath
    
    comp = Compilation()
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0

    challenge.compilation = comp

  def run(self, ex, ch):
    ch.returncode, ch.stdout, ch.stderr = self.execute("mono " + ch.rootpath + ex.mainfile + " " + ch.input_params)
