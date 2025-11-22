import re
from collections import Counter
from typing import List
from app.services.summarizer import _words, STOPWORDS, _sentences

def _top_keywords(text: str, n=10):
    wc = Counter(w for w in _words(text) if w not in STOPWORDS)
    return [w for w,_ in wc.most_common(n)]

def generate_mcq_from_keyword(keyword: str, text: str):
    # Very simple: present 3 distractors from top keywords + correct
    keys = _top_keywords(text, n=20)
    distractors = [k for k in keys if k != keyword][:3]
    choices = [keyword] + distractors
    # simple shuffle but keep deterministic for now
    return {
        "question": f"What is the best keyword or topic represented by: '{keyword}'?",
        "choices": choices,
        "answer": keyword
    }

def generate_tf_from_sentence(sentence: str):
    # create a true/false by negating a simple verb phrase (heuristic)
    question = f"True or False: {sentence.strip()}"
    # heuristically mark true
    return {"question": question, "answer": True}

def generate_quiz(text: str, num_mcq=5, num_tf=5):
    keywords = _top_keywords(text, n=50)
    mcqs = []
    for k in keywords[:num_mcq]:
        mcqs.append(generate_mcq_from_keyword(k, text))
    sents = _sentences(text)
    tfs = []
    for s in sents[:num_tf]:
        tfs.append(generate_tf_from_sentence(s))
    return {"mcqs": mcqs, "tfs": tfs}
