from .dockerenv import DockerEnv
from .summary import Summary
import re

class BaseProfessor(DockerEnv):

    def __init__(self, professor_name, template_filepath, stud_params, image_name="baseimg:v0"):
        super().__init__(image_name)
        self.r = re.compile('\s+')
        self.template_filepaths = template_filepath
        self.templates = []

        with open(template_filepath, "r") as fin:
            self.program = fin.read()
            self.stud_params = stud_params
            self.template_filepath = template_filepath
            self.stud_program = self.render(self.program, stud_params)
            
            self.professor_name = professor_name
            self.compilation_results = []
            self.execution_results = []
    
    def add_compilation(self, compilation):
        compilation.idd = len(self.compilation_results)
        self.compilation_results.append(compilation)

    def add_execution(self, execution):
        execution.idd = len(self.execution_results)
        self.execution_results.append(execution)
    
    def summary(self):
        sm = Summary()

        sm.num_compilations = len(self.compilation_results)
        sm.num_executions = len(self.execution_results)
        sm.num_correct_compilations = len([x for x in self.compilation_results if x.correctness == 1.0])
        sm.num_correct_executions = len([x for x in self.execution_results if x.correctness == 1.0])
        
        sm.professor_name = self.professor_name
        sm.image_name = self.image_name
        sm.program = self.program
        sm.stud_params = self.stud_params
        sm.stud_program = self.stud_program
        sm.compilations = self.compilation_results
        sm.executions = self.execution_results

        return sm

    def soft_compare(self, str1, str2):
        str1 = self.r.sub(" ", str1).strip()
        str2 = self.r.sub(" ", str2).strip()
        return str1 == str2
