import subprocess
import tempfile
import shlex
import uuid
import os


class DockerEnv:

    def __init__(self, image_name):
        self.idd = None
        self.image_name = image_name
        self.container_name = "DockerEnv_" + str(
                uuid.uuid4()).replace('-', '')
    
    def __enter__(self):
        cmd = "docker run --name %s -d %s" % (
                self.container_name, 
                self.image_name)
        
        result = subprocess.run(shlex.split(cmd), capture_output=True)
        result.check_returncode()
        self.idd = result.stdout.strip().decode('utf-8')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        cmd = "docker stop " + self.container_name
        subprocess.run(shlex.split(cmd), capture_output=True)
        
        cmd = "docker rm -f " + self.container_name
        subprocess.run(shlex.split(cmd), capture_output=True)
        
    def render(self, data, params):
        for k, v in params.items():
            data = data.replace("'" + k + "'", v)
        return data

    def make_executable(self, env_filepath):
        self.execute("chmod +x " + env_filepath)
    
    def create_file_from_template(self, env_filepath, local_template_filepath, template_parameters, make_executable=False):
    
        with open(local_template_filepath) as fin:
            content = self.render(fin.read(), template_parameters)
            self.create_file(env_filepath, content, make_executable)
    
    def create_file(self, env_filepath, content, make_executable=False):
        with tempfile.NamedTemporaryFile() as fout:
            fout.write(content.encode('utf-8'))
            fout.flush()
            self.send_file(fout.name, env_filepath)

        if make_executable:
            self.make_executable(env_filepath)
    
    def send_file(self, local_filepath, env_filepath, make_executable=False):
        dirname = os.path.dirname(env_filepath)

        cmd = "docker exec %s mkdir -p '%s'" % (self.container_name, dirname)
        subprocess.run(shlex.split(cmd))

        cmd = "docker cp %s %s:%s" % (local_filepath, self.container_name, env_filepath)
        subprocess.run(shlex.split(cmd))

        if make_executable:
            self.make_executable(env_filepath)
    
    def get_file(self, env_filepath, local_filepath):
        cmd = "docker cp %s:%s %s" % (
                self.container_name, 
                env_filepath, 
                local_filepath)
        
        subprocess.run(shlex.split(cmd))
    
    def execute(self, cmd):
        cmd = "docker exec -t " + self.container_name + " " + cmd
        r = subprocess.run(shlex.split(cmd), capture_output=True)
        returncode = r.returncode
        stdout = r.stdout.decode('utf-8')
        stderr = r.stderr.decode('utf-8')
        return returncode, stdout, stderr

