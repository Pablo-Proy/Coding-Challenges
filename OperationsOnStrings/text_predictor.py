
def text_predictor(repository,costumer_query):

    """
    This function returns a maximun of three suggested words (from a given repository) after each character of a keyword is typed by the costumer in the "search field".

    If there are more than three aceptable keywords, the functions returns the words that are first in alphabetical order. Furthermore, 
    the function starts suggesting keywords after the costumer has entered at least two characters.  
    """
    repository=[word.lower() for word in repository]
    repository.sort()
    costumer_query=costumer_query.lower()
    sugested_words=[]

    for i in range(1,len(costumer_query)):

        substring=costumer_query[:i+1]
        temporary_sugested_words=[]
        cont=0

        for word in repository:

            if word.find(substring)==0 and len(temporary_sugested_words)<3:

                temporary_sugested_words.append(word)
                cont+=1
            
        sugested_words.append(temporary_sugested_words)
    
    return sugested_words
