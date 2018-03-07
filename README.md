## AWS Systems Manager Document Generator

A utility to convert your Python or Bash programs into SSM documents (and optionally - CloudFormation templates, containing those documents).

You can find examples of command definitions in `src/ssm_document_generator/examples`.

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

## License

This library is licensed under the Apache 2.0 License. 
