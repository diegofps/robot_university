class Summary(dict):

    def __init__(self):

        self.professor_name = None
        self.num_challenges = None
        self.num_correct_challenges = None
        self.exercise = None
        self.challenges = []

    def show(self, include_programs=False):
        # import pdb; pdb.set_trace()
        
        print("--- EXERCISE ---")
        if self.exercise:
            self.exercise.show(2, include_programs)
        print()

        print("--- CHALLENGES ---")
        for ch in self.challenges:
            ch.show(2, include_programs)
        print()

        print("--- SUMMARY ---" )
        print("  professor_name:", self.professor_name)
        print("  num_challenges:", self.num_challenges)
        print("  num_correct_challenges:", self.num_correct_challenges)
        print()

