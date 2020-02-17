from setuptools import setup, find_packages
from setuptools.command.install import install

# see https://stackoverflow.com/a/29628540
# and https://github.com/USCDataScience/NLTKRest/blob/master/nltkrest/setup.py

def _post_install():
    import nltk
    nltk.download("popular")

class my_install(install):
    def run(self):
        #install.do_egg_install(self)
        #import nltk
        #nltk.download("popular")
        install.run(self)
        self.execute(_post_install, [], msg='running _post_install task')

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(name='mse-antede-fs2020-utilities',
      version='0.3',
      description='Utilities for AnTeDe course.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/markif/mse_antede_fs2020_utilities',
      author='Fabian',
      license='MIT',
      packages=['mse_antede_fs2020_utilities'],
      cmdclass={'install':my_install},
      install_requires=[
          'nltk',
          'numpy',
          'pandas',
          'contractions',
          'inflect',
          'beautifulsoup4',
      ],
      setup_requires=['nltk'],
      include_package_data=True,
      zip_safe=False)
