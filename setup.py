import setuptools

setuptools.setup(
    name='bbox',
    version='0.0.1',
    author='Konstantin Sebrovskiy',
    author_email='sebrovskiy.k@gmail.com',
    description='Objected management of bbox',
    url='https://github.com/SEBROVATER/bbox',
    license='MIT',
    packages=["bbox"],
    # install_requires=['numpy', "opencv-python", "imutils"],
    long_description=open('README.md').read(),
)
