from setuptools import setup, find_packages
from os.path import join, dirname
import holidays

setup(
    name='prod-cal',
    version=holidays.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    test_suite='tests',
    author='Vladimir Sidorov',
    author_email="vladimir.sidorov@raziogroup.com",
    maintainer='Vladimir Sidorov',
    maintainer_email="vladimir.sidorov@raziogroup.com",
    url='http://git.propercourse.ru'
)