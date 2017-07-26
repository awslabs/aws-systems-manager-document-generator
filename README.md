# SSMDocumentGenerator

This is a [BrazilPython 3](https://w.amazon.com/bin/view/BrazilPython3/) Python project.

## Building

Modifying the build logic of this package just requires overriding parts of the
setuptools process. The entry point is either the `release`, `build`, `test`, or
`doc` commands, all of which are implemented as setuptools commands in
the [BrazilPython-Base-3.0](https://code.amazon.com/packages/BrazilPython-Base/releases) 
package.

If you want to restrict the set of Python versions a package builds for, you can
do so by creating an executable script named `build-tools/bin/python-build` in
this package, and having it exit non-zero when the undesirable versions build.
By default this package will build for every version of Python in your
versionset.

The version strings that'll be passed in are:

* CPython##
* Jython##

Commands that only run for one version of Python will be run for the version in
the `default_python` argument to `setup()` in `setup.py`. `doc` is one such
command, and is configured by default to run the `doc_command` as defined in
`setup.py`, which will build Sphinx documentation.

## Testing

`brazil-build test` will run the test command defined in `setup.py`, by default `brazilpython_pytest`, which is defined in the [BrazilPython-Pytest-3.0](https://code.amazon.com/packages/BrazilPython-Pytest/releases) package. The arguments for this will be taken from `setup.cfg`'s `[tool:pytest]` section, but can be set in `pytest.ini` if that's your thing too. Coverage is enabled by default, provided by pytest-cov, which is part of the `PythonTestingDependencies` package group.

## Running

If you need to execute an interpreter, you will want to add a `test-dependency` on `Python = default`, which can then be run like so:

```
$(brazil-bootstrap --environmentType test-runtime)/bin/python
```

## Deploying

If this is a library, nothing needs to be done; it'll deploy the versions it builds. If you intend to ship binaries, add a dependency on [Python = default](https://devcentral.amazon.com/ac/brazil/directory/package/majorVersionSummary/Python?majorVersion=default) to `Config`, and then ensure that the right branch of `Python-default` is built into your versionset. You'll want either [CPython2](https://code.amazon.com/packages/Python/trees/CPython2) or [CPython3](https://code.amazon.com/packages/Python/trees/CPython3) for CPython.
