from setuptools import find_packages, setup
# find package look for every constructor file (__init__.py) and try to install that folder as local package
setup(
    name = 'gunDetection',
    version='0.0.0',
    author='Dhaivat',
    author_email='dhaivatpachchigar@gmail.com',
    packages=find_packages(),
    install_requires= [] 
)