"""Example tests."""

from myproject import __version__, hello


class TestVersion:
    """Tests for version information."""

    def test_version_is_string(self) -> None:
        """Version should be a string."""
        assert isinstance(__version__, str)

    def test_version_format(self) -> None:
        """Version should follow semantic versioning."""
        parts = __version__.split(".")
        assert len(parts) == 3
        assert all(part.isdigit() for part in parts)


class TestHello:
    """Tests for the hello function."""

    def test_hello_returns_string(self) -> None:
        """Hello should return a string."""
        result = hello()
        assert isinstance(result, str)

    def test_hello_is_greeting(self) -> None:
        """Hello should be a greeting."""
        result = hello()
        assert result.startswith("Hello")
