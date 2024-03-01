from setuptools import setup, find_packages


requires = ["requests-oauthlib==1.3.1"]
keywords = ["python", "Freee", "SDK", "Wrapper", "API"]


setup(
    name="python-freee-api",
    version="1.0.0",
    description="SlackやDiscord等のサーバを用いるアプリにFreeeAPIを組み込めるようにするラッパーです。",
    url="https://github.com/pochinoritaro/Freee",
    author="Kazuma Tsunomori",
    author_email="pochimoritaro@gmail.com",
    license="ISC, BSD, Apache 2.0, MPL-2.0, MIT",
    keywords=keywords,
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.12.1",
    ],
)