from multiprocessing import Pool

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

        for asset in self.exercise.assets:
            if asset.content is None:
                self.send_file(asset.local_filepath, asset.env_filepath)
            else:
                self.create_file(asset.content, asset.env_filepath)
    
    def deploy(self, ch):
        for template in self.exercise.templates:
            env_filepath = ch.rootpath + template.env_filepath

            if template.content is None:
                with open(template.local_filepath, "r") as fin:
                    program = fin.read()
            else:
                program = template.content

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

    def check_challenge_response(self, ch):
        # Overwrite this in case you want to customize correctness
        
        if ch.returncode != ch.expected_returncode:
            ch.issues_explanation.append("returncode is not correct")

        if not self.soft_compare(ch.stdout, ch.expected_stdout):
            ch.issues_explanation.append("stdout is not correct")
        
        if not self.soft_compare(ch.stderr, ch.expected_stderr):
            ch.issues_explanation.append("stderr is not correct")
        
        ch.correctness = 0.0 if ch.issues_explanation else 1.0

    def run(self, ex, ch):
        # Overwrite this in case you want to customize how to start the application (like java -jar ..., python3 ..., so on)
        ch.returncode, ch.stdout, ch.stderr = self.execute(ch.rootpath + ex.mainfile + " " + ch.input_params)

    def add_challenge(self, ch):
        ch.idd = len(self.challenges)
        ch.rootpath = "/challenges/" + str(ch.idd) + "/"
        self.challenges.append(ch)

    def mapper(self, ch):
        self.deploy(ch)
        self.run(self.exercise, ch)
        self.check_challenge_response(ch)
        return ch

    def summary(self):
        with Pool() as p:
            self.challenges = p.map(self.mapper, self.challenges)

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
