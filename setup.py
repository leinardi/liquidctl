import setuptools

repo_url = 'https://github.com/jonasmalacofilho/liquidctl'
version = '1.0.0'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = (fh.read().split('<!-- stop here for PyPI -->', 1)[0]
                        + 'Check the project page page for more information.')

setuptools.setup(
    name='liquidctl',
    version=version,
    author='Jonas Malaco',
    author_email='jonas@protocubo.io',
    description='Cross-platform tool and drivers for liquid coolers and other devices',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=repo_url,
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
    ],
    keywords='cross-platform driver nzxt kraken smart-device',
    project_urls={
        'Documentation': '{}/blob/v{}/README.md'.format(repo_url, version),
        'Changelog': '{}/blob/v{}/CHANGELOG.md'.format(repo_url, version),
    },
    install_requires=['docopt', 'pyusb'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'liquidctl=liquidctl.cli:main',
        ],
    },
)
