def build_lda_model(texts, num_topics):
    import gensim
    from gensim import corpora
    from gensim.models import LdaModel

    tokenized = [t.split() for t in texts]
    dictionary = corpora.Dictionary(tokenized)
    corpus = [dictionary.doc2bow(text) for text in tokenized]

    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42)

    return lda_model, corpus, dictionary