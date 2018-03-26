from app.app import run


def test_run():
    run('1', debug=True)
    assert 1 == 4

