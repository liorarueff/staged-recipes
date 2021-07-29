from distutils.core import setup, Extension
import distutils.command.bdist_conda

setup(
    name="pytorchnewtest",
    version="1.0",
    author="Liora Rueff",
    author_email="liora.rueff@gmail.com",
    url="https://github.com/liorarueff/pytorchnewtest",
    distclass=distutils.command.bdist_conda.CondaDistribution,
    conda_buildnum=1,
)
