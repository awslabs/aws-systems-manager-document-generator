import json

from ssm_document_generator.converter import Converter
import argparse

from pathlib import Path

DOCUMENT_EXTENSION = '.json'


def parse_arguments():
    parser = create_parser()
    return parser.parse_args()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("output", help="Output file or directory. Should match to input (e.g. if input is a file - "
                                       "this expected to be a file, correspondingly if input is directory - "
                                       "this is expected to be a directory).")
    parser.add_argument("-cf", "--cloud-formation",
                        help="Generate CloudFormation template instead of just SSM document",
                        action="store_true")
    parser.add_argument("--indent", help="Indent for resulting json for SSM document", type=int)
    return parser


def main():
    args = parse_arguments()

    input_path = validate_input_path(args.input)
    result = process_documents(input_path)

    if args.cloud_formation:
        output_cloudformation(args.output, result)
        return

    output_path = Path(args.output)
    return write_result(input_path, output_path, result, args.indent)


def write_result(input_path, output_path, results, indent=None):
    def get_document_json(document):
        return json.dumps(document, indent=indent, sort_keys=True)

    if input_path.is_file():
        if output_path.is_dir():
            print("Mismatch between input and output.")
            create_parser().print_help()
            exit(-1)

        output_path.write_text(get_document_json(results[0].ssm_document))
    else:
        for result in results:
            output_path.joinpath(result.document_definition['name'] + DOCUMENT_EXTENSION). \
                write_text(get_document_json(result.ssm_document))


def output_cloudformation(output, result):
    template = Converter.to_cloudformation(result)
    Path(output).write_text(template.to_json())


def process_documents(input_path):
    return Converter.convert_directory(input_path) if input_path.is_dir() else [Converter.convert(input_path)]


def validate_input_path(input_path_name):
    input_path = Path(input_path_name)
    if not input_path.exists():
        print('Specified input path does not exist')
        create_parser().print_help()
        exit(-1)
    return input_path


if __name__ == '__main__':
    main()
