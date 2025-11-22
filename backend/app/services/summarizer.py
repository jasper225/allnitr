import re
from collections import Counter
from typing import List

_SENTENCE_RE = re.compile(r'(?<=[.!?])\s+')

def _sentences(text: str) -> List[str]:
    parts = [s.strip() for s in _SENTENCE_RE.split(text) if s.strip()]
    return parts

def _words(text: str):
    return re.findall(r"\w+", text.lower())

STOPWORDS = {
  "the","and","is","in","to","of","a","for","on","with","that","this","as","are","by","an","be","or"
}

def simple_summarize(text: str, max_sentences: int = 5) -> str:
    sents = _sentences(text)
    if len(sents) <= max_sentences:
        return " ".join(sents)
    # score sentences by frequency of non-stopword tokens
    wc = Counter(w for w in _words(text) if w not in STOPWORDS)
    scores = []
    for i, s in enumerate(sents):
        score = 0
        for w in _words(s):
            score += wc.get(w, 0)
        scores.append((score, i, s))
    top = sorted(scores, reverse=True)[:max_sentences]
    # sort back into original order
    top_sorted = sorted(top, key=lambda x: x[1])
    return " ".join([t[2] for t in top_sorted])

def extract_bullets(summary: str):
    # simple split into sentences for bullets
    sents = _sentences(summary)
    return sents