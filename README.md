# megatranslate
A little CLI that translates text randomly between a bunch of languages and back, thereby completely messing with the legibility of the text.

### Downloadable Executable
To avoid installing dependencies you can get an executable file from the releases page in this repo.

### Build/Run from source
I recommend you create a virtualenv before doing the following steps:
```sh
git clone https://github.com/HyperCodec/megatranslate # get source code files
cd megatranslate
pip install -r requirements.txt # install dependencies
```

At this point, you should be set up to run it with `python3 main.py`. The following will build it to an executable:
```sh
pip install pyinstaller
./build.ps1
```
