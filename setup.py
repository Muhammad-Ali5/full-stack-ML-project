from setuptools import setup, find_packages
from typing import List


HYOEN_E_DOT = "-e ."
def get_requirements(file_path) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYOEN_E_DOT in requirements:
            requirements.remove(HYOEN_E_DOT)
    return requirements

setup(
    name="my_package",
    version="0.1.0",
    author="Muhammad Ali",
    author_email="maliuetm507@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)