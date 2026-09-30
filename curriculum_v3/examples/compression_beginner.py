import gzip


def compress_data(data):
    compressed_data = gzip.compress(data)
    return compressed_data


def restore_data(compressed_data):
    original_data = gzip.decompress(compressed_data)
    return original_data
