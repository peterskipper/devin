from setuptools import setup

setup(
    name='devin',
    version='0.1',
    url='https://github.com/peterskipper/devin',
    download_url='https://github.com/peterskipper/devin/archive/0.1.tar.gz',
    license='MIT',
    author='Peter Skipper',
    author_email='peter.skipper@gmail.com',
    description='Command line tool to recommend albums',
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'devin = devin.cli:main'
        ]
    }
)
