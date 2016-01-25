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