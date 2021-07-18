class Exercise:

    def __init__(self):
        
        self.image_name = None
        self.mainfile = None
        self.templates = []
        self.stud_params = {}
        self.assets = []

    def show(self, indentation, include_program=False):
        prefix = " " * indentation

        print(prefix + "image_name: " + self.image_name)
        print(prefix + "mainfile: " + self.mainfile)
        print(prefix + "templates: " + str(self.templates))
        print(prefix + "stud_params: " + str(self.stud_params))
        print(prefix + "assets: " + str(self.assets))
        print()