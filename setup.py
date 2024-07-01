from setuptools import find_packages,setup
from typing import List

HYPHER_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requiements=[]
    with open(file_path) as file_obj:
        requiements=file_obj.readlines()
        requiements = [req.replace("\n","") for req in requiements]

        if HYPHER_E_DOT in requiements:
            requiements.remove(HYPHER_E_DOT)
    return requiements

setup(
    name="ml-project-workflow",
    version="0.0.1",
    author="Naman Garg",
    author_email="namangarg2075@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)