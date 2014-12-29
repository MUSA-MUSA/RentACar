import math
import re
from cars.models import Car

# Create a list of words to ignore
STRIP_WORDS_ENG = ['a','an','and','by','for','from','in','no','not', 'of','on','or','that','the','to','with']
STRIP_WORDS_TR = ['ve','ile']

def get_tokens(str):
    """Break a string into tokens, preserving URL tags as an entire token.

       This implementation does not preserve case.
       Clients may wish to override this behavior with their own tokenization.
    """
    return re.findall(r"<a.*?/a>|<[^\>]*>|[\w'@#]+", str.lower())

def get_cars():
    cars = list(Car.objects.all())
    return cars



def calculate_tf(term):
    """

    this is find fequncy of wordsdgsdg
    """
    tf_scores = {}
    cars = get_cars()
    for car in cars:
        t_terms = get_tokens(car.Modele) # title
        d_terms = get_tokens(car.Notes) # description

        tf_t = t_terms.count(term)/float(len(t_terms))
        tf_scores[car] = tf_t

    return tf_scores

def calculate_idf(term):
    count = 0
    cars = get_cars()
    for car in cars:
        if term in car.Modele or term in car.Notes:
            count += 1
    if count > 0:
        return 1.0 + math.log(float(len(cars)) / count)
    else:
        return 1.0


def calculate_tfidf(term):
    tf = calculate_tf(term)
    idf = calculate_idf(term)
    tf_idf = {}
    for car in tf:
        tf_idf[car] = tf[car]*idf
    return tf_idf

def return_results(term):
    terms = get_tokens(term)
    if len(terms) == 1:
        res = calculate_tfidf(terms[0])
        results = res.items()
        result = sorted(results, key=lambda x: x[1] ,reverse=True)
    elif len(terms) > 1:
        pass

    return result


