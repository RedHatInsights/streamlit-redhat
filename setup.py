from setuptools import setup


setup(
    name="streamlit-redhat",
    version="0.1",
    description="Utility functions to work with Streamlit in Red Hat",
    url="http://github.com/RedHatInsights/streamlit-redhat",
    author="Juan Díaz",
    author_email="jdiazsua@redhat.com",
    packages=["streamlit_redhat"],
    install_requires=[
        'streamlit',
        'Authlib',
        'watchdog',
        'pyjwt[crypto]',
    ],
    zip_safe=False,
)
