try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Zeko',
    'author': 'Barbara',
    'url': '',
    'download_url': '',
    'author_email': 'barbara.erdec@gmail.com',
    'version': '1.0',
    'install_requires': ['pytest'],
    'packages': ['zeko'],
    'scripts': ['src'],
    'name': 'projectzeko'
}

setup(**config)
