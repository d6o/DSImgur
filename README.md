# DSImgur

Easily download images, Albums and entire profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!

![](https://i.imgur.com/ytEp7fG.gif)

## Features

- Download Single Images ex.: https://imgur.com/EJtc5ox or http://i.imgur.com/EJtc5ox.jpg
- Download Entire Albums ex.: https://imgur.com/a/GpDQW or https://imgur.com/gallery/GpDQW
- Download Entire PROFILES ex.: https://imgur.com/user/ytho34/ or https://imgur.com/account/ytho34/
- Written in uncomplicated Python
- Easily download files in the fastest speed possible
- Up to 452% faster than traditional download using Multi-Threaded Downloads
- Easy to [install](https://github.com/DiSiqueira/DSImgur#installation)
- Stupidly [easy to use](https://github.com/DiSiqueira/DSImgur#usage)
- Uses natives libs
- Option to organize your files
- Download 100 files in less than 40s

## Installation

### Option 1: [Pip](https://pip.pypa.io/en/stable/installing/)

```bash
$ pip install DSImgur
```

### Option 2: From source

```bash
$ git clone https://github.com/DiSiqueira/DSDownload.git
$ cd DSDownload/
$ python setup.py install
```

## Usage

### Basic usage

```bash
# Download a file
$ dsdownload https://i.imgur.com/eUrbKtO.jpg
```

### Download using Workers

```bash
# Download 3 files using 2 Workers
$ dsdownload --workers 2 https://i.imgur.com/eUrbKtO.jpg https://i.imgur.com/9am20SK.jpg https://i.imgur.com/KR06C.jpg
```

### Combine everything

```bash
# Download 3 files using 2 Workers and put on my-images folder
$ dsdownload --output my-images --workers 2 https://i.imgur.com/eUrbKtO.jpg https://i.imgur.com/9am20SK.jpg https://i.imgur.com/KR06C.jpg
```

## Program Help

![](https://i.imgur.com/0EXBDFM.png)

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/DiSiqueira/DSDownload/issues) to report any bugs or file feature requests.

### Developing

PRs are welcome. To begin developing, do this:

```bash
$ git clone --recursive git@github.com:DiSiqueira/DSDownload.git
$ cd DSDownload/DSDownload/
$ python DSDownload.py
```

## Social Coding

1. Create an issue to discuss about your idea
2. [Fork it] (https://github.com/DiSiqueira/DSDownload/fork)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request
7. Profit! :white_check_mark:

## License

The MIT License (MIT)

Copyright (c) 2013-2015 Diego Siqueira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.




















# Imgur
A perfect Imgur Downloader

## Requirements

* [Python](https://www.python.org)

## Usage

```bash
Imgur.py [-h] [--threads THREADS] [--output OUTPUT] urls [urls ...]

A perfect Imgur Downloader.

positional arguments:
  urls               URLs to be downloaded

optional arguments:
  -h, --help         show this help message and exit
  --threads THREADS  Number of parallel downloads. The default is 5.
  --output OUTPUT    Output folder
```

###Example 1
```bash
 python Imgur.py https://imgur.com/gallery/0vs7ne8
```
###Example 2
```bash
 python Imgur.py --threads 2 https://imgur.com/gallery/bqT8w https://imgur.com/a/0vs7ne8
```
###Example 3
```bash
 python Imgur.py --threads 2 --output myimages https://imgur.com/NE6j4u3 https://imgur.com/gallery/bqT8w https://imgur.com/a/0vs7ne8 https://i.imgur.com/V0UW3P0.webm
```

## Find a bug/issue or simply want to request a new feature?

[Create a Github issue/feature request!](https://github.com/DiSiqueira/Imgur/issues/new)