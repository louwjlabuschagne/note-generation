# note-generation

## Instalation
### OSX
On OSX you need to install `portaudio` from homebrew

```
brew install portaudio 
```

Then the magic command:

```
pip3 install pyaudio --global-option="build_ext" --global-option="-I/usr/local/include" --global-option="-L/usr/local/lib"
```