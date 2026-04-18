from setuptools import setup
import pathlib
import re


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

version = ''

with open('lavaplay/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')


setup(
    name='lavaplay-glimpse.py',
    version=version,
    description='Fork of lavaplay.py made for glimpse. Original repository: https://github.com/HazemMeqdad/lavaplay.py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vladpochuev/lavaplay.py',
    author='vladpochuev',
    author_email='pochuev.vladislav@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='lavalink, discord, discord-lavalink, lavaplay, lavaplay.py',
    packages=["lavaplay"],
    install_requires=["aiohttp"],
    project_urls={
        'Source': 'https://github.com/vladpochuev/lavaplay.py',
        'Original source': 'https://github.com/HazemMeqdad/lavaplay.py'
    },
)
