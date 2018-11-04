## AWS Systems Manager Document Generator

A library + DSL that allows you to easily define SSM documents and convert you your Python or Bash programs into SSM documents (and optionally - CloudFormation templates, containing those documents).

You can find examples of command definitions in `src/ssm_document_generator/examples`.

## Workflow

**Option 1. Calling the generator directly:** 

1. Create a definition file.   
   The file can either directly contain the commands you want to execute or can point to a Python or a Bash file that serves as entry point for your program.
   You can find an example of definition file [here](src/ssm_document_generator/examples/get_file/get_file_definition.py)
1. Run the program and point it at the definition file you've created. I.e. if we are to use it with the definition mentioned above we'd do something like:  
   `python main.py get_file_definition.py get_file.json`  
   `get_file.json` here is the output file where the resulting SSM document would be written to.
   You can see the description of other available options below.

**Option 2. Integrate the document creation into your package build process:**

If you have a Python package with several SSM command definitions present - you can integrate the document creation into your build process by using [build tasks](src/ssm_document_generator/build_tools) provided with this package.  
You would do that by adding the following into your `setup.py`:
```python
#...
setup(
#...
cmdclass={
          'ssm_generator': SSMGenerator,
          'install_scripts': SSMGeneratorBuild
      },
#...
)

```

## Command usage:

```
usage: main.py [-h] [-cf] [--indent INDENT] input output

positional arguments:
  input                 A definition file or a directory containing multiple definition files.
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
