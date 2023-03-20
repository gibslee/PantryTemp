import pathlib
from setuptools import setup

readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="pantry_temp",
    version="0.0",
    packages=['pantry', ],
    description="A repository for storing Python scripts to run pantry fridge monitors",
    package_data={"pantry": ["*"]},
    include_package_data=True,
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Gibson Lee',
    author_email='a@a.a',
    url='https://github.com/gibslee/PantryTemp',
    license='PublicDomain',
    install_requires=[],
)
