from t04 import Phonemes
from t04 import Syllable
from t04 import Phonetic_array_generator

vowels = {
    "a": {"unrounded", "open", "back"},
    "i": {"unrounded", "close", "front"},
    "u": {"rounded", "close", "back"},
    "e": {"unrounded", "mid", "front"},
    "o": {"rounded", "mid", "back"},
}

heb_consonants = {
    "’": {"voiceless", "glottal", "plosive"},
    "b": {"voiced", "bilabial", "plosive"},
    "g": {"voiced", "velar", "plosive"},
    "d": {"voiced", "dental", "plosive"},
    "h": {"voiceless", "glottal", "fricative"},
    "w": {"voiced", "bilabial", "approximant"},
    "z": {"voiced", "dental", "fricative"},
    "ḥ": {"voiceless", "velar", "fricative"},
    "ṭ": {"voiceless", "dental", "plosive"},
    "y": {"voiced", "palatal", "approximant"},
    "k": {"voiceless", "velar", "plosive"},
    "l": {"voiced", "dental", "lateral approximant"},
    "m": {"voiced", "nasal", "bilabial"},
    "n": {"voiced", "dental", "nasal"},
    "s": {"voiceless", "dental", "fricative"},
    "‘": {"voiceless", "laryngael", "plosive"},
    "p": {"voiceless", "bilabial", "plosive"},
    "ṣ": {"voiceless", "dental", "affricate"},
    "q": {"voiceless", "laryngael", "plosive"},
    "r": {"voiced", "dental", "trill"},
    "š": {"voiceless", "alveolar", "fricative"},
    "t": {"voiced", "dental", "plosive"},
}

consonants = {
    "k": {"voiceless", "velar", "plosive"},
    "g": {"voiced", "velar", "plosive"},
    "s": {"voiceless", "dental", "fricative"},
    "z": {"voiced", "dental", "fricative"},
    "t": {"voiceless", "dental", "plosive"},
    "d": {"voiced", "dental", "plosive"},
    "f": {"voiceless", "labiodental", "fricative"},
    "v": {"voiced", "labiodental", "fricative"},
    "n": {"voiced", "dental", "nasal"},
    "h": {"voiceless", "glottal", "fricative"},
    "p": {"voiceless", "bilabial", "plosive"},
    "b": {"voiced", "bilabial", "plosive"},
    "m": {"voiced", "bilabial", "nasal"},
    "j": {"voiced", "palatal", "approximant"},
    "r": {"voiced", "alveolar", "tap"},
    "l": {"voiced", "dental", "lateral approximant"},
    "w": {"voiced", "bilabial", "approximant"},
    "": {None},
}

params = {
    "obstrunt_coda": True,
    "head_initial": True,
    "null_onset": True,
    "NP_initial": True,
    "ccluster_size": 2,
    "vcluster_size": 2,
}

heb_params = {
    "ccluster_size": 2,
    "vcluster_size": 1,
}

phonemes = Phonemes(consonants, vowels)
syllable = Syllable(phonemes, params)
gentor = Phonetic_array_generator(syllable)

heb_phonemes = Phonemes(heb_consonants, vowels)
heb_syllable = Syllable(heb_phonemes, heb_params)
heb_gentor = Phonetic_array_generator(heb_syllable)

lst = []
for i in range(128):
    lst.append(gentor.gen_naive_multiple())
print(lst)
