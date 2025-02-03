from setuptools import setup, find_packages

setup(
    name="coursegen",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "coursegen = coursegen.cli:main"
        ]
    },
    package_data={"coursegen": ["*.json"]},  # Ensure JSON files are included
    include_package_data=True,
)
