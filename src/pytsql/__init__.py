"""`Pytsql` allows to run mssql sripts, typically run via GUIs, via CLI."""


from .tsql import execute, executes

__version__ = "1.1.0"

__all__ = ["execute", "executes"]
