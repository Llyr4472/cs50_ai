import nltk
import sys
import os
from string import punctuation
from math import log

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for file in os.listdir(directory):
        with open(os.path.join(directory, file),"r",encoding="utf-8") as f:
            files[file] = f.read()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    document = document.lower()
    tokens = nltk.tokenize.word_tokenize(document)
    for token in tokens.copy():
        if token in punctuation or token in nltk.corpus.stopwords.words("english"):
            tokens.remove(token)
    return tokens


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    wf = {}
    idfs = {}
    for document in documents:
        for word in documents[document]:
            if word in wf.keys():
                wf[word] += 1
            else:
                wf[word] = 1
    for word in wf:
        idfs[word] = log(len(documents)/wf[word])
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idf = {}
    for file in files:
        tf_idf[file] = 0
        for word in query:
            tf= files[file].count(word)
            tf_idf[file] += idfs[word] + tf
    return sorted(tf_idf)[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    ranked_sentences = {}
    for sentence in sentences:
        idf,wd = 0.0,0.0
        for word in query:
            idf += idfs[word]
            wd += sentence.count(word)/len(sentence)
        ranked_sentences[sentence] = (idf,wd)
    return sorted(ranked_sentences,reverse=True)[:n]


if __name__ == "__main__":
    main()
