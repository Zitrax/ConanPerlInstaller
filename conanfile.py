from conans import ConanFile, tools
from winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey
import os


class PerlinstallerConan(ConanFile):
    """
    For now this installs for all users with all default settings.
    A possible improvement would be to use the portable install packages
    to make a local install instead.
    """
    name = "Perl_installer"
    version = "1.0"
    url = "https://github.com/Zitrax/ConanPerlInstaller"
    description = "Installer for Strawberry Perl"
    license = "GNU Public License"
    settings = {"os": ["Windows"], "arch": ["x86_64"]}
    options = {"version": ["5.26.0.1"]}
    default_options = "version=5.26.0.1"

    def isInstalled(self):
        """Check if perl is already installed"""
        try:
            reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            k = OpenKey(reg, r'SOFTWARE\Classes\Perl_program_file\shell\Execute Perl Program\command')
            self.output.info("Perl already installed: true")
            return True
        except WindowsError:
            self.output.info("Perl already installed: false")
        return False
        
    def build(self):
        if self.isInstalled():
            return
        #url = "http://strawberryperl.com/download/{0}/strawberry-perl-{0}-64bit.msi".format(self.options.version)
        url = "http://bengtssons.info/files/strawberry-perl-5.26.0.1-64bit.msi"
        dest = "perl.msi"
        self.output.info("Will download " + url)
        tools.download(url, dest)
        self.run("msiexec /i {} /qb".format(os.path.abspath('perl.msi')))

    def package(self):
        """We currently install globally so have nothing to package"""
        pass
