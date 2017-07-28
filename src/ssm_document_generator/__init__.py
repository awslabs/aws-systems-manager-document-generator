import json

from ssm_document_generator.converter import Converter
import argparse

from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("--indent", help="Indent for resulting json for SSM document", type=int)
    return parser.parse_args()


def main():
    # todo work with input directories - discovery.
    args = parse_arguments()
    ssm_document = Converter.convert(Path(args.input))
    result = json.dumps(ssm_document, indent=args.indent, sort_keys=True)
    if args.output:
        with Path(args.output).open(mode='w') as output_file:
            output_file.write(result)
    else:
        print(result)


if __name__ == '__main__':
    main()
