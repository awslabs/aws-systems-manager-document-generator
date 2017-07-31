def include_filter(lines, filter_list):
    if not filter_list:
        return lines

    return filter(lambda line: any(word in line for word in filter_list),
                  lines)


def exclude_filter(lines, filter_list):
    if not filter_list:
        return lines

    return filter(lambda line: all(word not in line for word in filter_list),
                  lines)
