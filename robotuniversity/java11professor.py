from .baseprofessor import BaseProfessor
from .compilation import Compilation
import os

class Java11Professor(BaseProfessor):

  def __init__(self, exercise):
    if exercise.image_name is None:
      exercise.image_name = "openjdk11image:v0"
    
    super().__init__("Java11Professor", exercise)
  
  def compile(self, exercise, challenge):
    manifest = None
    compiled_sources = []
    sources = []

    for x in exercise.assets:
      if x.env_filepath.endswith(".java"):
        sources.append(challenge.rootpath + x.env_filepath)
      
      elif x.env_filepath.endswith(".class"):
        compiled_sources.append(challenge.rootpath + x.env_filepath)

      elif x.env_filepath.endswith(".mf"):
        manifest = challenge.rootpath + x.env_filepath
      
    for x in exercise.templates:
      if x.env_filepath.endswith(".java"):
        sources.append(challenge.rootpath + x.env_filepath)

      elif x.env_filepath.endswith(".class"):
        compiled_sources.append(challenge.rootpath + x.env_filepath)
        
      elif x.env_filepath.endswith(".mf"):
        manifest = challenge.rootpath + x.env_filepath
    
    output_filepath = challenge.rootpath + exercise.mainfile
    output_folderpath = os.path.dirname(output_filepath)

    self.create_folder(output_folderpath)
    
    comp = Compilation()
        
    cmd = "javac " + " ".join(sources)
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    compiled_sources += [x[:-5] + ".class" for x in sources]
    compiled_sources = [x.replace(challenge.rootpath, '') for x in compiled_sources]

    cmd = "jar -c -f " + output_filepath

    if manifest is not None:
      cmd += " -m " + manifest
    
    cmd += " -C " + challenge.rootpath + " " + " ".join(compiled_sources)
    
    comp.returncode, comp.stdout, comp.stderr = self.execute(cmd)
    comp.correctness = 1.0 if comp.returncode == 0 else 0.0

    challenge.compilation = comp

  def run(self, ex, ch):
    ch.returncode, ch.stdout, ch.stderr = self.execute("java -jar " + ch.rootpath + ex.mainfile + " " + ch.input_params)
