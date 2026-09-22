import random
def sample(deck,seed):
    if not deck:
        return None
    rng=random.Random(seed)
    return rng.choice(deck),rng.randint(0,10),rng.random()
