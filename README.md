#  Indian Express News Topic Modeling

This is a Streamlit-based web application for performing **unsupervised topic modeling** on news articles from *The Indian Express*. It leverages **Latent Dirichlet Allocation (LDA)** from the Gensim library to discover hidden themes in textual content. The application provides an intuitive GUI for uploading data, cleaning text using NLTK, and interactively exploring topics.

---

##  Features

- Upload CSV files containing news articles
- Automatic text preprocessing (lowercasing, punctuation removal, stopword removal, lemmatization)
- Interactive slider to select the number of LDA topics
- Real-time topic extraction and display
- Dark-themed modern UI using custom Streamlit styling

---

##  Technologies Used

- Python
- Streamlit
- Gensim (LDA Modeling)
- NLTK (Text Cleaning and Lemmatization)
- Pandas

---

##  Dataset Format

The CSV file must contain at least one of the following columns:
- `text` (preferred)
- `content` (will be automatically renamed to `text`)

Each row should represent a single news article.

---

##  Installation

1. **Clone the repository**  
```bash
git clone https://github.com/GuhanManimaran/Topic_Modelling.git
cd Topic_Modelling
