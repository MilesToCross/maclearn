from setuptools import find_packages, setup
from typing import List

def get_requirements(a:str)->List[str]:
    with open(a) as b:
        c=b.readlines()
        c=[i.replace("\n","") for i in c]
        
        if "-e ." in c:
            c.remove("-e .")
    return c




setup(
    name= "maclearn",
    version="0.0.1",
    author="Ankit Swain",
    author_email="ankitswain4982@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)