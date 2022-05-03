from setuptools import setup, find_packages
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

INSTALL_REQUIRES = [
    "click==8.0.1",
    "youtube-dl==2021.12.17"
]

if __name__ == '__main__':
  # Setting up
  setup(
      name='ytext',
      version='0.1.1',
      author='Gabriel Braico Dornas',
      author_email='gabrielbdornas@gmail.com',
      description='Python package to convert youtube videos to text',
      long_description_content_type="text/markdown",
      long_description=open('README.md', encoding='utf-8').read() + '\n\n' + open('CHANGELOG.md', encoding='utf-8').read(),
      url="https://github.com/gabrielbdornas/ytext",
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      keywords=['python', 'youtube', 'transcripiton'],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ],
      entry_points="""
        [console_scripts]
        ytext=ytext.cli:cli
      """
  )