from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='teacherspayteachers',
    version='0.1.0',
    description='Convert Teacherspayteachers posts to Pinterest posts',
    long_description=readme,
    author='Sarah Gonzalez',
    url='https://github.com/sarahmgonzalez/teacherspayteachers_pinterest',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)