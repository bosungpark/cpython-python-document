"""
pre-setting

xcode-select --install
brew install openssl xz zlib gdbm sqlite

cd cpython   
CPPFLAGS="-I$(brew --prefix zlib)/include"     
LDFLAGS="-L$(brew --prefix zlib)/lib"   
./configure --with-openssl=$(brew --prefix openssl)

make -j2 -s  
"""
