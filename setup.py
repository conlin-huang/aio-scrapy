from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'aioscrapy/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

install_requires = [
    "aiohttp",
    "w3lib",
    "parsel",
    "PyDispatcher",
    'zope.interface>=4.1.3'
    "redis>=4.3.1",
]
extras_require = {}

setup(
    name='aio-scrapy',
    version=version,
    url='https://github.com/conlin-huang/aio-scrapy.git',
    description='A high-level Web Crawling and Web Scraping framework based on Asyncio',
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding='utf-8').read(),
    author='conlin',
    author_email="995018884@qq.com",
    license="MIT",
    packages=find_packages(exclude=('example',)),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['aioscrapy = aioscrapy.cmdline:execute']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    install_requires=install_requires,
    extras_require=extras_require,
    keywords=[
        'aio-scrapy',
        'scrapy',
        'aioscrapy',
        'scrapy redis',
        'asyncio',
        'spider',
    ]
)
