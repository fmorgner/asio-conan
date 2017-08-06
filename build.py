# pylint: disable=missing-docstring
from conan.packager import ConanMultiPackager


def main():
    builder = ConanMultiPackager(
        username='fmorgner',
        archs=['x86_64'],
        upload='https://api.bintray.com/conan/fmorgner/conan-fmorgner',
        remotes='https://api.bintray.com/conan/fmorgner/conan-fmorgner',
    )
    builder.add()
    builder.run()


if __name__ == '__main__':
    main()
