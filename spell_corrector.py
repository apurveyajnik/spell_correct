import numpy as np
import itertools

def words(text):
    out_dict = {}
    for line in text.split("\n"):
        line = line.split("\t")
        out_dict[line[0]] = int(line[1])
    return out_dict

WORDS = words(open('count_1w.txt').read())

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    if word in WORDS:
        return WORDS[word] / N
    else:
        return 0.0

def correction(word): 
    "Most probable spelling correction for word."
    if " " in word:
        words = word.split(" ")
        sep = " "
    elif "-" in word:
        words = word.split("-")
        sep = "-"
    elif len(joined_word(word))==2:
        words = joined_word(word)
        sep = ""
    else:
        words = [word]
        sep = ""

    top_cands = []
    for word in words:
        cands = list(set(candidates(word)))
        print("Candidates : ", cands)
        probs = [P(c) for c in cands]
        sort_ids = np.argsort(probs)[::-1]
        top_cands.append([cands[i] for i in sort_ids[:10]])
    if len(words)==2:
        corrections =  list(map(sep.join, itertools.product(top_cands[0], top_cands[1])))
    else:
        corrections = top_cands[0]
    return corrections


def candidates(word): 
    "Generate possible spelling corrections for word."
    word = word.lower()

    e1 = edits1(word)
    e2 = edits2(word)
    return (known([word]) or known(e1) or known(e2) or [word])



def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word` or joined by mistake"
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def joined_word(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    special_single_letters = "iao"
    for w1, w2 in splits:
        if known(w1) and known(w2) and (len(w1)>1 or w1 in special_single_letters):
            return [w1, w2]
    else:
        return [word]

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

if __name__ == '__main__':
    print(correction('speling'))
    print(correction('korrectud'))
    print(correction('bycyclerounl'))
    print(correction('homeAssignment'))
    print(correction('aschool'))