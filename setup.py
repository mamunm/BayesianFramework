import setuptools

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

with open('README.md', 'r') as f:
    readme = f.read()

setuptools.setup(
    name="BayesianFramework",
    version="0.1",
    url="https://github.com/mamunm/BayesianFramework",

    author="Osman Mamun",
    author_email="mamunm@stanford.edu",

    description="A framework for Bayesian model selection (BMS) and Bayesian"
    description += " model Averaging (BMA).",
    long_description=readme,
    license='GPL-3.0',

    packages=[
        'bayesframe',
    ],
    package_dir={'bayesframe': 'bayesframe'},
    entry_points='''
         [console_scripts]
      ''',
    install_requires=requirements,
    python_requires='>=3.6.8',

    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Machine Learning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ],
)
