from setuptools import setup

import versioneer

version=versioneer.get_version()
cmdclass=versioneer.get_cmdclass()

setup(name='when-changed',
      version=version,
      cmdclass=cmdclass,
      description='Run a command when a file is changed',
      author='Johannes H. Jensen',
      author_email='joh@pseudoberries.com',
      url='https://github.com/joh/when-changed',
      packages=['whenchanged'],
      entry_points={
            'console_scripts': ('when-changed = whenchanged.whenchanged:main')
      },      install_requires=['watchdog'],
      license='BSD'
      )
