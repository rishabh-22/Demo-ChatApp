import nltk
from nltk.tokenize import word_tokenize


data = {'CC': 'Coordinating conjunction',
        'CD': 'Cardinal digit',
        'DT': 'Determiner',
        'EX': 'Existential ',
        'FW': 'Foreign word',
        'IN': 'Preposition',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List marker',
        'MD': 'Modal',
        'NN': 'Noun, singular',
        'NNS': 'Noun plural',
        'NNP': 'Proper Noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'TO': 'TO',
        'UH': 'Interjection',
        'VB': 'Verb',
        'VBD': 'Verb',
        'VBG': 'Verb',
        'VBN': 'Verb',
        'VBP': 'Verb',
        'VBZ': 'Verb',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-abverb'}


def make_tags_from_sentence(text):
    tokenized = word_tokenize(text)
    tagged = nltk.pos_tag(tokenized)
    answer = {}
    for word in tagged:
        try:
            answer[word[0]] = data[word[1]]
        except KeyError:
            pass
    # print(tagged)
    return answer


# make_tags_from_sentence('John likes the blue house at the end of the street')
