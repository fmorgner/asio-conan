# pylint: disable=missing-docstring
from conans import ConanFile


class ASIOConan(ConanFile):
    name = 'Asio'
    description = (
        'Asio is a cross-platform C++ library for network and low-level I/O '
        'programming that provides developers with a consistent asynchronous '
        'model using a modern C++ approach.'
    )
    version = '1.10.8'
    settings = None
    url = 'https://github.com/fmorgner/asio-conan.git'
    author = 'Felix Morgner (felix.morgner@gmail.com)'
    license = 'Boost Software License, Version 1.0'

    def _get_tag(self):
        return 'asio-{version}'.format(**{
            'version': self.version.replace('.', '-'),
        })

    def source(self):
        self.run('git clone https://github.com/chriskohlhoff/asio.git')
        self.run('cd asio && git checkout %s' % self._get_tag())

    def package(self):
        self.copy('*.hpp', src='asio/asio/include', dst='include')
        self.copy('*.ipp', src='asio/asio/include', dst='include')

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.defines = ['-DASIO_STANDALONE']
