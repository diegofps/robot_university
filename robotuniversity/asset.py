class Asset:

  def __init__(self, local_filepath=None, env_filepath=None, content=None):

    self.local_filepath = local_filepath
    self.env_filepath = env_filepath
    self.content = content

    if env_filepath is None:
      raise RuntimeError("env_filepath must not be None")

    if local_filepath is None and content is None:
      raise RuntimeError("local_filepath and content can not be both None")

    if env_filepath.startswith("/"):
      raise RuntimeError("env_filepath must no be an absolute path")
