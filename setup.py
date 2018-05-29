"""
A cli package for accessing and quering arxiv papers.
"""
from setuptools import find_packages, setup

dependencies = ['click', 'feedparser', 'tableprint']

setup(
    name='arxivcli',
    version='0.1.0-beta',
    url='https://github.com/olamyy/arxivcli',
    license='BSD',
    author='Olamilekan Wahab',
    author_email='olamyy53@gmail.com',
    description='A cli package for accessing and quering arxiv papers.',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'arxivcli = arxivcli.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
