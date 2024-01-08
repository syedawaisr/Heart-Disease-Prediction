
'''
use this file to install as 
python install setup.py or pip install .

this will create a whole project as a package and will not cause importing errors from one file to another
'''
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Heart-Disease-Project',
    version='0.0.1',
    author='Awais Raza',
    author_email='muhammadowais296@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)