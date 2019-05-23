from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

PKG_NAME = "jimi"
VERSION = "0.1.0"
PKG_DESCRIPTION = "Midi-powered musician"
AUTHOR = "Madeline Wolf"
INSTALL_REQUIRES = ["mido==1.2.9", "python-rtmidi==1.3.0"]

if __name__ == "__main__":
    setup(
        name=PKG_NAME,
        version=VERSION,
        description=PKG_DESCRIPTION,
        long_description=readme,
        author=AUTHOR,
        license=license,
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=INSTALL_REQUIRES,
        python_requires=">=3.6.2",
        entry_points={
            "console_scripts": ["jimi=jimi.jimi:main"],
        },
    )
