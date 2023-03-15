from setuptools import find_packages, setup


with open("README.md") as f:
    long_description = f.read()

INSTALL_REQUIRES = [
    "fastapi==0.89.1",
    "loguru==0.5.3",
    "numpy==1.21.6",
    "optuna==3.1.0",
    "pyarrow==6.0.1",
    "pydantic==1.10.4",
    "joblib==1.2.0",
    "pandas==1.3.5",
    "scikit-learn==1.0.2",
    "uvicorn==0.20.0",
    "lightgbm==3.3.2",
]

if __name__ == "__main__":
    setup(
        name="autolgbm",
        description="autolgbm: tuning lightgbm with optuna",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Rishiraj Acharya",
        author_email="heyrishiraj@gmail.com",
        url="https://github.com/rishiraj/autolgbm",
        license="Apache 2.0",
        package_dir={"": "src"},
        packages=find_packages("src"),
        entry_points={"console_scripts": ["autolgbm=autolgbm.cli.autolgbm:main"]},
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        platforms=["linux", "unix"],
        python_requires=">=3.6",
    )
