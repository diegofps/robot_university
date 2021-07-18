
class Compilation:

  def __init__(self):
    self.correctness = 1.0
    self.returncode = 0
    self.stdout = ""
    self.stderr = ""
  
  def show(self, indentation, include_program=False):
    prefix = " " * indentation

    print()
    print(prefix + "Compilation:")
    
    print(prefix + "  correctness: " + str(self.correctness))

    print(prefix + "  returncode: " + str(self.returncode))
    print(prefix + "  stdout: " + self.stdout)
    print(prefix + "  stderr: " + self.stderr)

    if include_program:
        print(prefix + "  prof_program: " + self.prof_program)
    