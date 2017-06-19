from conans import ConanFile
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "Zitrax")


class PerlinstallerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Perl_installer/1.0@%s/%s" % (username, channel)

    def build(self):
        self.output.success("Test build() ok")
    
    def imports(self):
        self.output.success("Test imports() ok")

    def test(self):
        self.output.success("Test test() ok")
