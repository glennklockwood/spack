from spack import *


class Dtbuild1(Package):
    """Package for use as a build tool for deptypes testing which has its own
    deptree"""

    homepage = "http://www.example.com"
    url = "http://www.example.com/dtbuild1-1.0.tar.gz"

    version('1.0', '0123456789abcdef0123456789abcdef')

    depends_on('dtbuild2', deptypes='build')
    depends_on('dtlink2')
    depends_on('dtrun2', deptypes='run')

    def install(self, spec, prefix):
        pass