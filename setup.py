from setuptools import setup, find_packages


setup(
    name='dlc_api',
    packages=find_packages(where='src'),
    package_data={
        "dlc_api.package_data": ["*"],
    },
    entry_points={
        'console_scripts': [
            'dlc_api = dlc_api:run',
        ]
    },
    version='0.1',
    license='MIT',
    description = 'My package description',
    description_file = "README.md",
    author="Julien Braine",
    author_email='julienbraine@yahoo.fr',
    url='https://github.com/JulienBrn/dlc_api',
    download_url = 'https://github.com/JulienBrn/dlc_api.git',
    package_dir={'': 'src'},
    keywords=['python'],
    install_requires=["beautifullogger", "pandas"],
    #['pandas', 'matplotlib', 'PyQt5', "sklearn", "scikit-learn", "scipy", "numpy", "tqdm", "beautifullogger", "statsmodels", "mat73", "psutil"],
    python_requires=">=3.10"
)
