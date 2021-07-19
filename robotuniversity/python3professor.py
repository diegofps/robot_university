from .baseprofessor import BaseProfessor

class Python3Professor(BaseProfessor):

    def __init__(self, exercise):
        if exercise.image_name is None:
            exercise.image_name = "python3image:v0"
        
        super().__init__("Python3Professor", exercise)
    
    def run(self, ex, ch):
        ch.returncode, ch.stdout, ch.stderr = self.execute("python3 " + ch.rootpath + ex.mainfile + " " + ch.input_params)
