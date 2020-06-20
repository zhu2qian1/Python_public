# class Consonants:
#     def __init__(self, consonants: dict):
#         self.d = consonants

#     def save(self, destination):
#         import json

#         pass

#     def load(self, destination):
#         import json

#         pass

#     def search(self, conditions: set) -> list:
#         return []

#     def pickrandom(self, num=1) -> str:
#         from random import choice

#         return str([])

lang1_path = r".\\lang1\\lang1.json"


def choice_conditioned(s: dict, c: set, n: int) -> str:
    """returns n-sized string under the given condition (c) from s (dictionary)."""
    from random import choice
    result = []
    for _ in range(n):
        result.append(choice([x for x in s if c < set(s[x])]))
    return "".join(result)


def pickrandom(seq, n=1) -> str:
    raise NotImplementedError  # Bug found, fix needed
    from random import choices

    return "".join(choices(seq, k=n))


def save(path: str, dictionary: dict):
    import json
    with open(path, "w") as f:
        json.dump(dictionary, f, indent=4)


def load(path) -> dict:
    import json
    with open(path, "r") as f:
        return json.load(f)


consonants = {
    "p": ["voiceless", "bilabial", "stop", "elongable"],
    "f": ["voiceless", "labiodental", "fricative"],
    "t": ["voiceless", "dental", "plosive", "elongable"],
    "s": ["voiceless", "dental", "fricative"],
    "k": ["voiceless", "velar", "plosive", "elongable"],
    "h": ["voiceless", "glottal", "fricative"],
    "w": ["voiced", "bilabial", "approximant"],
    "m": ["voiced", "bilabial", "nasal"],
    "b": ["voiced", "bilabial", "plosive"],
    "n": ["voiced", "dental", "nasal"],
    "d": ["voiced", "dental", "plosive"],
    "j": ["voiced", "palatal", "approximant"],
    "g": ["voiced", "velar", "plosive"],
}

vowels = {
    "a": ["open", "central", "unrounded"],
    "i": ["close", "front", "unrounded"],
    "u": ["close", "back", "rounded"],
}

phonemes = {
    "consoants": consonants,
    "vowels": vowels, }