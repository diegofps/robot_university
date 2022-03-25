from .baseprofessor import BaseProfessor
from .compilation import Compilation
import os

class CPPProfessor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "clangimage:v0"
    
    super().__init__("CPPProfessor", exercise)
  
  def compile(self, exercise, challenge):
    sources = [challenge.rootpath + x.env_filepath for x in exercise.templates if x.env_filepath.endswith(".cpp")]
    sources += [challenge.rootpath + x.env_filepath for x in exercise.assets if x.env_filepath.endswith(".cpp")]
    output_filepath = challenge.rootpath + exercise.mainfile
    output_folderpath = os.path.dirname(output_filepath)

    self.create_folder(output_folderpath)
    cmd = "clang++ " + " ".join(sources) + " -o " + output_filepath

    comp = Compilation()
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0
    
    challenge.compilation = comp

  # def add_challenge(self, ch):

  #   # Copy and render the template files into the container, compile if necessary
  #   self.deploy(ch)

  #   # Execute the exercise with current execution parameters
  #   ch.returncode, ch.stdout, ch.stderr = self.execute(self.exercise.mainfile + " " + ch.input_params)

  #   # Add respose to summary
  #   self.add_challenge_result(ch)
