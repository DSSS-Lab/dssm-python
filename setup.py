from setuptools import setup, find_packages

setup(
    name='dssm_python',
    version='1.0.0',
    author="Louis Schraeder",
    author_email="z524037@shibaura-it.ac.jp",
    description = "Python interface for DSSM",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/DSSS-Lab/dssm-python.git",
    license="MIT",
    license_files=('LICENSE',),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    packages=find_packages(include=['dssm_python', 'dssm_python.*']),
    install_requires=[
        'sysv-ipc ',
    ],
    include_package_data=True,
)