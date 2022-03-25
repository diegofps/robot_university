from robotuniversity.template import Template
from robotuniversity.asset import Asset

class Exercise:

    def __init__(self):
        
        self.image_name = None
        self.mainfile = None
        self.templates = []
        self.stud_params = {}
        self.assets = []

    def add_template(self, *args, **params):
        template = Template(*args, **params)
        self.templates.append(template)
    
    def add_asset(self, *args, **params):
        template = Asset(*args, **params)
        self.assets.append(template)
    
    def show(self, indentation, include_program=False):
        prefix = " " * indentation

        print(prefix + "image_name: " + self.image_name)
        print(prefix + "mainfile: " + self.mainfile)

        print(prefix + "templates:")
        for template in self.templates:
            print(prefix + "  " + str(template))

        print(prefix + "stud_params:")
        for key, value in self.stud_params.items():
            print(prefix + "  " + key + "='" + value + "'")

        print(prefix + "assets: " + str(self.assets))
        print()
