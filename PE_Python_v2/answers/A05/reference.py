import pickle,gzip
def dump_state(state):
    return gzip.compress(pickle.dumps(state,protocol=pickle.HIGHEST_PROTOCOL))
def load_state(blob):
    return pickle.loads(gzip.decompress(blob))
