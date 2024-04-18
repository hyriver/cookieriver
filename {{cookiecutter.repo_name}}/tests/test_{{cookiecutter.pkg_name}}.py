import io
import {{cookiecutter.pkg_name}} as {{cookiecutter.pkg_short_name}}

def test_function():
    {{cookiecutter.pkg_short_name}}.function()
    assert True

def test_show_versions():
    f = io.StringIO()
    {{cookiecutter.pkg_short_name}}.show_versions(file=f)
    assert "SYS INFO" in f.getvalue()