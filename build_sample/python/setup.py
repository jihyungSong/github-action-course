from setuptools import setup, find_packages

setup(
    name='humancat',
    version='0.0.3',
    description='GitHub Action Build Test Sample',
    author='YOUR_NAME',
    author_email='YOUR_EMAIL@EMAIL_ADDR',
    url='https://github.com/YOUR_REPO/github-action-course',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['sample', 'cat', 'human', 'humancat'],
    python_requires='>=3.8',
    package_data={},
    zip_safe=False
)
