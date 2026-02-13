from setuptools import setup, find_packages

with open("README.md", 'r', encoding='UTF-8') as f:
      long_description = f.read()

__version__ = '0.0.0.0'

REPO_NAME = "VisaEligibilityPredictor-AU"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "visaPrediction"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"


setup(
      name="Visa Grant Prediction",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End ML implementation for austrila visa grant prediction",
      long_description=long_description,
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=find_packages(where='src')
)