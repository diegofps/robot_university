#!/usr/bin/python3

from robotuniversity.dockerenv import DockerEnv


def test_basic_command(de):
    print("--- Executing a basic command inside the environment ---")

    r = de.execute("ls -lah /")

    print("returncode:", r.returncode)
    print("stdout:", r.stdout.decode('utf-8'))
    print("stderr:", r.stderr.decode('utf-8'))
    print()


def test_file_from_string(de):
    print("--- Creating a python3 file from scratch and running it ---")
    
    content = "#!/usr/bin/python3\nprint(\'Hello World')"
    de.create_file("/app/demo.py", content, True)
    r = de.execute("/app/demo.py")

    print("returncode:", r.returncode)
    print("stdout:", r.stdout.decode('utf-8'))
    print("stderr:", r.stderr.decode('utf-8'))
    print()


def test_file_from_template(de):
    print("--- Creating a python3 file from template and running it ---")

    tp = {
        "STUD.IMPORTS": "import math",
        "STUD.FUNCTIONS": "def secret(a):\n  return math.sin(a) * math.cos(a+10)",
        "STUD.SECRET_NAME": "secret"
    }
    
    de.create_file_from_template("/app/demo2.py", "./assets/demo2.template.py", tp, True)
    r = de.execute("/app/demo2.py")

    print("returncode:", r.returncode)
    print("stdout:", r.stdout.decode('utf-8'))
    print("stderr:", r.stderr.decode('utf-8'))
    print()


def test_send_local_file(de):
    print("--- Sending a local python3 file and running it ---")

    de.send_file("./assets/demo3.py", "/app/demo3.py", True)
    r = de.execute("/app/demo3.py")
    
    print("returncode:", r.returncode)
    print("stdout:", r.stdout.decode('utf-8'))
    print("stderr:", r.stderr.decode('utf-8'))
    print()


with DockerEnv("baseimg:v0") as de:
    test_basic_command(de)
    test_file_from_string(de)
    test_file_from_template(de)
    test_send_local_file(de)

