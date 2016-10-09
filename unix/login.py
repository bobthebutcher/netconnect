import pexpect
import logging

from netconnect.base import BaseLogin
from netconnect.helpers import (
    validate_login_type,
    clean_up_error,
    PEXPECT_ERRORS
)


class UnixLogin(BaseLogin):
    def login(self, login_type='ssh'):
        """
        Login to linux/unix shell (bash terminal assumed)
        :param connector: Connector object
        :param login_type: SSH or Telnet
        :return: pexpect spawn object

        Authentication types:
         - username and password
         - certificate based
        """
        validate_login_type(login_type)

        login_cmd = self.ssh_driver if login_type.lower() == 'ssh' else self.telnet_driver

        child = pexpect.spawn(login_cmd)
        i = child.expect(PEXPECT_ERRORS + ['.*#', '.*$', '.*assword.*'])
        if i == (0 or 1):
            raise i
        elif i == (2 or 3):
            return child
        elif i == 4:
            child.sendline(self.password)
            j = child.expect(PEXPECT_ERRORS + ['.*#', '.*$'])
            if j == (0 or 1):
                raise i
            elif j == (2 or 3):
                return child