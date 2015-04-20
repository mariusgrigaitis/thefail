from setuptools import setup, find_packages


setup(name='thefail',
      version=1.12,
      description="Magnificent app which corrects your previous console command",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/thefail',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pathlib', 'psutil'],
      entry_points={'console_scripts': [
          'thefail = thefail.main:main']})
