from .compilation import Compilation
from .dockerenv import DockerEnv
from .summary import Summary
import re

class BaseProfessor(DockerEnv):

    def __init__(self, professor_name, exercise):
        super().__init__(exercise.image_name)

        self.r = re.compile('\s+')
        self.exercise = exercise
        self.challenges = []
        self.professor_name = professor_name
        self.never_compiled = True

        for local_filepath, env_filepath in self.exercise.assets:
            self.send_file(local_filepath, env_filepath)
    
    def deploy(self, ch):
        if not self.never_compiled and not ch.prof_params:
            return 

        for local_filepath, env_filepath in self.exercise.templates:
            with open(local_filepath, "r") as fin:
                program = fin.read()

                if self.exercise.stud_params:
                    program = self.render(program, self.exercise.stud_params)

                if ch.prof_params:
                    program = self.render(program, ch.prof_params)
                
                self.create_file(env_filepath, program)
        
        self.compile(self.exercise, ch)
        self.never_compiled = False

    def compile(self, exercise, challenge):
        # Overwrite this in case this source needs custom compiling (like c,cpp, java, csharp, ...)
        challenge.compilation = Compilation()

    def add_challenge(self, execution):
        execution.idd = len(self.challenges)
        self.challenges.append(execution)
    
    def summary(self):
        sm = Summary()

        sm.num_challenges = len(self.challenges)
        sm.num_correct_challenges = len([x for x in self.challenges if x.correctness == 1.0])
        
        sm.professor_name = self.professor_name
        sm.exercise = self.exercise
        sm.challenges = self.challenges

        return sm

    def soft_compare(self, str1, str2):
        str1 = self.r.sub(" ", str1).strip()
        str2 = self.r.sub(" ", str2).strip()
        return str1 == str2
