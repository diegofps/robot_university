class Summary(dict):

    def __init__(self):

        self.professor_name = None
        self.num_compilations = None
        self.num_executions = None
        self.num_correct_compilations = None
        self.num_correct_executions = None
        self.image_name = None
        self.program = None
        self.stud_params = None
        self.stud_program = None
        self.compilations = []
        self.executions = []

    def show(self, include_programs=False):
        print("--- SUMMARY ---" )
        print("  professor_name", self.professor_name)
        print("  num_compilations", self.num_compilations)
        print("  num_executions", self.num_executions)
        print("  num_correct_compilations", self.num_correct_compilations)
        print("  num_correct_executions", self.num_correct_executions)
        print()

        print("--- COMPILATIONS ---")
        for comp in self.compilations:
            comp.show(2, include_programs)
        print()

        print("--- EXECUTIONS ---")
        for ex in self.executions:
            ex.show(2, include_programs)
        print()
