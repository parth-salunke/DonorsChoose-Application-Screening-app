import setuptools

#whenever we pubish project it will run this code to show readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

#Project info
REPO_NAME = "DonorsChoose-Application-Screening-app"
AUTHOR_USER_NAME = "parth-salunke"
SRC_REPO = "donorschoose"
AUTHOR_EMAIL = "paarthsalunke@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Donor choose application screening Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)