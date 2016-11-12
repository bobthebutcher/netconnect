import pytest

from netconnect.helpers import parse_error, validate_login_type
from pexpect.exceptions import EOF, TIMEOUT


def test_parse_error_raises_eof():
    with pytest.raises(EOF):
        parse_error(0)


def test_parse_error_eof_message():
    with pytest.raises(EOF) as e:
        parse_error(0)
        assert e.value.message == 'Got EOF'


def test_parse_error_raises_timeout():
    with pytest.raises(TIMEOUT):
        parse_error(1)


def test_parse_error_timeout_message():
    with pytest.raises(TIMEOUT) as e:
        parse_error(1)
        assert e.value.message == 'Got Timeout'


def test_validate_login_type_raises_value_error():
    with pytest.raises(ValueError):
        validate_login_type('invalid')


def test_validate_login_type_with_telnet_does_not_raise_value_error():
    assert validate_login_type('telnet') is True


def test_validate_login_type_with_ssh_does_not_raise_value_error():
    assert validate_login_type('ssh') is True
