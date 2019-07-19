import os
try:
    # Python 3
    from unittest.mock import patch, MagicMock
except ImportError:
    # Python 2
    from mock import patch, MagicMock  # noqa: F401

from gbdx_task_interface import GbdxTaskInterface


def test_base_paths():

    def os_path_exists(path):
        if path.rstrip('/') in ('/mnt/work', '/mnt/work/input', '/mnt/work/output'):
            return True
        return False

    os.path.exists = MagicMock(side_effect=os_path_exists)

    t = GbdxTaskInterface()

    # Base paths
    assert t.base_path == '/mnt/work/'
    assert t.input_path == '/mnt/work/input'
    assert t.output_path == '/mnt/work/output'


def test_ports():
    # Data port paths
    def os_path_isdir(path):
        if path.rstrip('/') == '/mnt/work/input/my_data_port':
            return True
        return False

    os.path.isdir = MagicMock(side_effect=os_path_isdir)

    t = GbdxTaskInterface()

    my_data_port_path = t.get_input_data_port('my_data_port')
    assert my_data_port_path == '/mnt/work/input/my_data_port'
