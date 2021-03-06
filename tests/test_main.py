import space
import beyond


def test_as_package(run):
    """Invocation of the space command via python packages

    use the ```if __name__ == "__main__"``` at the bottom of the 
    __main__.py file
    """

    r = run("python -m space")
    assert r.stdout
    assert not r.stderr
    assert not r.success


def test_list_subcommands(run):
    """The space command without argument display the list of
    available subcommands and options
    """

    r = run("space")

    data = {}
    mode = "subcommands"
    for line in r.stdout.splitlines()[3:]:
        if not line:
            continue
        elif line == "Available addons sub-commands :":
            mode = "addons"
            continue
        elif line == "Options :":
            mode = "options"
            continue

        subdict = data.setdefault(mode, {})

        k, _, v = line.strip().partition(" ")
        subdict[k] = v.strip()

    assert len(data['subcommands']) == 12
    assert len(data['options']) == 5
    assert not r.stderr
    assert not r.success


def test_version(run):

    r = run("space --version")

    lines = r.stdout.splitlines()

    assert len(lines) == 2
    assert lines[0].split() == ["space-command" , space.__version__]
    assert lines[1].split() == ["beyond" , beyond.__version__]

    assert not r.stderr
    assert not r.success
