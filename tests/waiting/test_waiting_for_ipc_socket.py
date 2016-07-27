import pytest
from flaky import flaky

import gevent

from pygeth.geth import DevGethProcess


def test_waiting_for_ipc_socket(base_dir):
    with DevGethProcess('testing', base_dir=base_dir) as geth:
        assert geth.is_running
        geth.wait_for_ipc(timeout=60)


@flaky(max_runs=3)
def test_timeout_waiting_for_ipc_socket(base_dir):
    with DevGethProcess('testing', base_dir=base_dir) as geth:
        assert geth.is_running
        with pytest.raises(gevent.Timeout):
            geth.wait_for_ipc(timeout=0.1)
        assert geth.is_running