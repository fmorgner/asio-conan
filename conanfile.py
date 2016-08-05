from conans import ConanFile
from re import search

class ASIOConan(ConanFile):
    name = 'Asio'
    version = '1.10.6'
    settings = None
    url = 'https://github.com/fmorgner/asio-conan.git'
    author = 'Felix Morgner (felix.morgner@gmail.com)'
    license = 'Boost Software License, Version 1.0'

    def _get_tag(self):
        return 'asio-%s' % self.version.replace('.', '-')

    def source(self):
        self.run('git clone https://github.com/chriskohlhoff/asio.git')
        self.run('cd asio && git checkout %s' % self._get_tag())

    def build(self):
        pass

    def package(self):
        self.copy('*.hpp', src='asio/asio/include', dst='include')
        self.copy('*.ipp', src='asio/asio/include', dst='include')
