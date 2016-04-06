from setuptools import setup, find_packages
from os.path import join, dirname
import prodcal

setup(
    name='prod-cal',
    version=prodcal.__version__,
    packages=find_packages(),
    description='Given module allows to use production calendars of different countries',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    test_suite='tests',
    author='Vladimir Sidorov',
    author_email="vladimir.sidorov@raziogroup.com",
    maintainer='Vladimir Sidorov',
    maintainer_email="vladimir.sidorov@raziogroup.com",
    url='http://git.propercourse.ru',
    license='Apache 2.0',
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'License :: Freeware',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Office/Business',
                 'Topic :: Office/Business :: Scheduling',
                 'Topic :: Utilities'],

)