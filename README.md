# SSMDocumentGenerator

This package allows you to convert your Python or Bash programs into SSM documents
 (and optionally - CloudFormation templates, containing those documents).

You can find examples of command definitions in `src/ssm_document_generator/examples`.

You can find an example of using this package in combination with `CfnBuild` in `OwlsInfrastructure` package.  

Usage:

```
usage: main.py [-h] [-cf] [--indent INDENT] input output

positional arguments:
  input                 Input file or directory
  output                Output file or directory. Should match to input (e.g.
                        if input is a file - this expected to be a file,
                        correspondingly if input is directory - this is
                        expected to be a directory).

optional arguments:
  -h, --help            show this help message and exit
  -cf, --cloud-formation
                        Generate CloudFormation template instead of just SSM
                        document
  --indent INDENT       Indent for resulting json for SSM document
```
