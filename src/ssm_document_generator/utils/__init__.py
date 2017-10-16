def dict_without_none_entries(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}
