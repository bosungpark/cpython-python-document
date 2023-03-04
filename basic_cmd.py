"""
xcode-select --install
brew install openssl xz zlib gdbm sqlite

cd cpython   
CPPFLAGS="-I$(brew --prefix zlib)/include"     
LDFLAGS="-L$(brew --prefix zlib)/lib"   
./configure --with-openssl=$(brew --prefix openssl)

make -j2 -s  -> this cmd compiles file, or simply use "make" without options
./python.exe -> this is python bin file

make altinstall -> this cmd make usable my independent version of python or "sudo make altinstall"
"""
