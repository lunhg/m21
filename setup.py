from distutils.core import setup
from src.info import Info

setup(
    name=Info.getName(),
    version=Info.getVersion(),
    description=Info.getDescription(),
    author="\n".join([k for (k, v) in Info.getAuthors().items()]),
    author_email="\n".join([k for (k, v) in Info.getAuthors().items()]),
    py_module=['']
)
