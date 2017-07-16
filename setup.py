import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'PYPIREADME.rst')).read()
REQUIREMENTS = [
    line.strip() for line in open(os.path.join(os.path.dirname(__file__),
                                               'requirements.txt')).readlines()]

setup(name='rlyehian',
      version='0.1',
      long_description=README,
      url='https://github.com/JLDevOps/Rlyehian',
      author='JLDevops',
      author_email='jldevops@gmail.com',
      license='MIT License',
      packages=['rlyehian'],
      install_requires=REQUIREMENTS,
      zip_safe=False
      )
