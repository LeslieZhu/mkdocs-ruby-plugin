from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-ruby-plugin",
    version="0.0.3",
    description="An MkDocs plugin to add pinyin/furigana to Chinese/Japanese Kanji text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs ruby plugin",
    url="https://github.com/lesliezhu/mkdocs-ruby-plugin",
    author="Leslie Zhu",
    author_email="pythonisland@gmail.com",
    license="Apache-2.0",
    python_requires=">=3.9",
    install_requires=[
        "mkdocs>=1.4.1",
    ],
    packages=["mkdocs_ruby_plugin"],
    entry_points={
        "mkdocs.plugins": [
            "ruby = mkdocs_ruby_plugin.plugin:RubyPlugin",
        ],
    },
)
