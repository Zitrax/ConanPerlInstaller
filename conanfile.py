from conans import ConanFile, tools
from winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey
import os


class PerlinstallerConan(ConanFile):
    """
    Download and unzips portable strawberry perl
    """
    name = "Perl_installer"
    version = "1.0"
    url = "https://github.com/Zitrax/ConanPerlInstaller"
    description = "Installer for Strawberry Perl"
    license = "GNU Public License"
    settings = {"os": ["Windows"], "arch": ["x86_64"]}
    options = {"version": ["5.26.0.1"]}
    default_options = "version=5.26.0.1"

    def build(self):
        url = "http://strawberryperl.com/download/{0}/strawberry-perl-{0}-64bit-portable.zip".format(self.options.version)
        dest = "perl.msi"
        self.output.info("Will download " + url)
        tools.download(url, dest)
        tools.unzip(dest, "unzipped")

    def package(self):
        self.copy("*", dst="", src="unzipped")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "perl", "bin"))
