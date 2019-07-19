def test_import():
    try:
        from gbdx_task_interface import GbdxTaskInterface
        assert GbdxTaskInterface
    except ImportError:
        assert False, 'Could not import package'
