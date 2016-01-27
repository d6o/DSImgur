from DSImgur.config import version, description, name, github
from distutils.core import setup

setup(
  name = name,
  packages = [name], 
  version = version,
  description = description,
  author = 'Diego Siqueira',
  author_email = 'dieg0@live.com',
  url = github + '/' + name,
  download_url = github + '/'+ name + '/tarball/' + version, 
  keywords = ['download', 'thread', 'imgur', 'pictures', 'albums', 'simple', 'profile', 'wrap'],
  classifiers = [],
  license='MIT',
  entry_points = {
          'console_scripts': [
              'dsimgur = DSImgur.DSImgur:main',                  
          ],              
      },

  install_requires=[
      'dsdownload',
  ],
)