import re
import mmap
import pickle
import numpy as np
from collections import defaultdict, OrderedDict

def dd_list():
    return defaultdict(list)

def pmi(xy, x, y):
    return np.log(xy) - np.log(x) - np.log(y)
def entropy(p):
    return np.log(p) * -p

def save_model(model, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(model, fw)


def load_model(filename):
    with open(filename, 'rb') as fr:
        model = pickle.load(fr)
    return model

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines
#for idx, line in enumerate(tqdm(fi, total=get_num_lines(input_file)), 1):

def contain_english(str0):
    return bool(re.search('[a-z]', str0))

def contain_digital(str0):
    return bool(re.search(r'\d', str0))

def contain_katakana(str0):
    return bool(re.search(u"[\u30a0-\u30ff]+", str0))

def contain_hiragana(str0):
    return bool(re.search(u"[\u3040-\u309f]+", str0))

def generate_ngram(input_list, n):
    result = []
    for i in range(1, n+1):
        result.extend(zip(*[input_list[j:] for j in range(i)]))
    return result