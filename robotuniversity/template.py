from .asset import Asset

class Template(Asset):
  def __init__(self, *args, **params):
    super().__init__(*args, **params)
