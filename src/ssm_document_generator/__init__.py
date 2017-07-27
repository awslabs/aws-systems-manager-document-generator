import json
import pprint

from ssm_document_generator.converter import Converter
import argparse

from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser()
    # https://docs.python.org/3/howto/argparse.html
    parser.add_argument("-o", "--output", help="Output file/directory?")
    parser.add_argument("-f", "--file", help="Input file")
    return parser.parse_args()

    # todo make file/directory specifications mutually exclusive

    # discover files with definitions in args[1]
    #     args[2] pretty?
    # input file
    # output file


if __name__ == '__main__':
    """discover files with definitions in args[1]
    args[2] pretty?
    """

    args = parse_arguments()
    # pprint.pprint(ssm_converter.converter.Converter().convert(Path(args.file)))
    ssm_document = Converter().convert(Path(args.file))
    print(ssm_document)
    with Path("../ssm_to_upload.json").open(mode='w') as output_file:
        json.dump(ssm_document, output_file, indent=4, sort_keys=True)
