# About this project

This is a MVP for a machine teaching implementation capable of running multiple languages. It uses docker to encapsulate the language environment containing the compiler / interpreter.

# Dependencies

1. docker - You must have the docker daemon on your local machine in order to create images and execute containers. If you don't have it, follow the installation instructions from the official docker website.

2. python3 - This project requires python3

# Running it

Step 1. Clone the repository

```shell
git clone git@github.com:diegofps/robot_university.git
cd robot_university
```

Step 2. Build the images

```shell
cd docker_images
docker build -t baseimg:v0 baseimg
docker build -t clangimage:v0 clangimage
docker build -t openjdk11image:v0 openjdk11image
docker build -t monoimage:v0 monoimage
docker build -t python3image:v0 python3image
cd ..
```

Step 3. Run a test for the desired language

```shell
python3 test_cprofessor.py
python3 test_cppprofessor.py
python3 test_csharpprofessor.py
python3 test_java11professor.py
python3 test_python3professor.py
```

# Known issues

> Docker may remove your local images in order to keep your disk's free space. In some cases, specially after not using one of the images for a while, you may need to build them again.
