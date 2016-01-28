from setuptools import setup

setup(
  name = 'DSImgur',
  version = '1.0.0.2',
  description = 'Easily download images, Albums, Galleries and entire Profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!',
  url = 'https://github.com/DiSiqueira/DSImgur',
  author = 'Diego Siqueira',
  author_email = 'dieg0@live.com',
  license = 'MIT',
  package_dir = { 'DSImgur' : 'src' },
  packages = [ 'DSImgur' ],
  zip_safe = False, 
  keywords = ['download', 'thread', 'speed', 'resume', 'multi', 'simple', 'imgur', 'album', 'gallery', 'images'],
  entry_points = 
  {
      'console_scripts': 
      [
          'dsimgur = DSImgur:main',
      ],
  },
  install_requires = ['DSDownload']
)