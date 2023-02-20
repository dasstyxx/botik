import os


def concat_paths(source, destination):
    """
    Concatenate two paths.
    :param source: Source absolute path
    :param destination: Destination relative path
    :return: concatenated path
    """

    def fix_prefix(x): return x if x.startswith('/') else '/' + x

    destination = destination.lstrip('/')
    if destination.startswith('~'):
        destination = destination[1:]
        return fix_prefix(destination)

    # TODO: make a better OS-independent path handling
    combined_path = os.path.normpath((os.path.join(source, destination)))
    combined_path = str(combined_path).replace('\\', '/')
    return fix_prefix(combined_path)
