from pathlib import Path


def get_definitions(base_directory_path):
    """
    For given directory return all .definition files in it and its subdirectories.
    """
    return Path(base_directory_path).glob('**/*.definition')
