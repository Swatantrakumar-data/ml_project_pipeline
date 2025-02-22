from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath: str)-> List[str]:
    requirements = []

    with open(filepath, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n','') for i in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

setup(name='ML_PROJECT_PIPELINE',
      version='0.0.1',
      description='ML pipeline project',
      author='Swatantra Kumar',
      author_email='swatantrakumar17082000@gmail.com',
      
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')

     )