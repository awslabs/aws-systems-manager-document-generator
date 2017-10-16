import importlib.util


def load_module(module_path):
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path.resolve())
    definition_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(definition_module)
    return definition_module


def dict_without_none_entries(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}
