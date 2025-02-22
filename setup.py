# -*- coding: utf-8 -*-

import setuptools

from inventree_bulk.version import BULK_PLUGIN_VERSION

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="inventree-bulk-plugin",

    version=BULK_PLUGIN_VERSION,

    author="wolflu05",

    author_email="76838159+wolflu05@users.noreply.github.com",

    description="Bulk creation plugin for InvenTree",

    long_description=long_description,

    long_description_content_type='text/markdown',

    keywords="inventree bulk",

    url="https://github.com/wolflu05/inventree-bulk-plugin",

    license="MIT",

    packages=setuptools.find_packages(),

    install_requires=[
        "pydantic"
    ],

    setup_requires=[
        "wheel",
        "twine",
    ],

    python_requires=">=3.6",

    entry_points={
        "inventree_plugins": [
            "BulkActionPlugin = inventree_bulk.bulk_plugin:BulkActionPlugin"
        ]
    },
)
