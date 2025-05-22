def clean_text(text):
    import re
    import string
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer

    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()

    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [w for w in tokens if not w in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return ' '.join(tokens)