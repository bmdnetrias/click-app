# {{ cookiecutter.hyphenated }}

{% if cookiecutter.github_username %}
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/releases)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/blob/master/LICENSE)
{% endif %}

{{ cookiecutter.description }}

## Installation

Install this tool using a standard virtual environment:

	$ git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.underscored }}
	$ python3 -m venv .{{ cookiecutter.underscored }}
	$ source .{{ cookiecutter.underscored }}/bin/activate
	(.{{ cookiecutter.underscored }}) $ pip3 install --upgrade -e ./{{ cookiecutter.underscored }} pip
	(.{{ cookiecutter.underscored }}) $ {{ cookiecutter.underscored }}

    pip install {{ cookiecutter.hyphenated }}
	
Using `pipx`

	# https://pipx.pypa.io/stable/installation/
	$ brew install pipx
	$ pipx ensurepath
    $ pipx install "{{ cookiecutter.underscored }} @ git+ssh://git@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.underscored }}" 
	$ {{ cookiecutter.hyphenated }}
	
Using `uv`

    # https://docs.astral.sh/uv/getting-started/installation/
    $ brew install uv
    $ uv tool install "{{ cookiecutter.underscored }} @ git+ssh://git@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.underscored }}"
	$ {{ cookiecutter.hyphenated }}
	

## Usage

For help, run:

    {{ cookiecutter.hyphenated }} --help

You can also use:

    python -m {{ cookiecutter.underscored }} --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd {{ cookiecutter.hyphenated }}
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
