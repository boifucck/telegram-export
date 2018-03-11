"""Setup for telegram-export"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.rst", "r") as readme:
    desc=readme.read()

setup(
    name='telegram-export',
    version='0.1.0',
    description='A tool to download Telegram data (users, chats, messages, '
                'and media) into a database (and display the saved data).',
    long_description=desc,
    url='https://github.com/expectocode/telegram-export',
    author='expectocode and Lonami',
    author_email='expectocode@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MPL License',
        'Programming Language :: Python :: 3',
    ],
    keywords='Telegram messaging database',
    packages=find_packages(),
    install_requires=['tqdm', 'telethon-aio', 'appdirs'],
    entry_points={  # Optional
        'console_scripts': [
            'telegram-export=telegram_export:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/expectocode/telegram-export/issues',
        'Source': 'https://github.com/expectocode/telegram-export'
    }
)
