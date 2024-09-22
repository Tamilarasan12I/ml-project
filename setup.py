from setuptools import find_packages,setup
from  typing import List
hed = '-e.'

def get_requirements(file_path:str)->list[str]:
    ...
    this function will return the list of requirements
    ...
    requirements=[]
    with open (file_path)as file_obj:
        requirements = file.obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
    if hed in requirements:
        requirements.remove(hed)
    return requirements


setup(
    name='ml-project',
    version='1.0.0',
    author='Tamilarasan',
    author_email='djtamilktm@gmail.com',
    package = find_packages(),
    install_requires= get_requriements('requirements.txt')
)