#this script is a draft to extract proper names from a string
#it mainly focuses on personal names, but this will also catch some corporate names too
#(this can pose a problem if you only want people's names, but you can add corporate stopwords to a stopword list)

#note 1: this does not pull them in order, it just pulls them

#note 2: the regexs need to be ordered by least likely to be matched to most likely to be matched, for any new patterns added in

#this will need many more regex patterns added to account for all name-pattern variations
#I have tried to make the pattern names descriptive of the patterns, i.e. "initialdot_last_suffixdot" corresponds to names like "J. Mascis Jr.", "first_initial_apostrophiclast" to "S. O'Connor", "first_initialdot_last" to "Mary J. Blige", "first_last" to "Kim Gordon", etc. etc.

def pn_extractor(string):
    initialdot_last_suffixdot = '([A-Z]\.\s[A-Z][a-z]{1,}\s[A-Z][a-z]\.)'
    first_initial_apostrophiclast = '([A-Z][a-z]{1,}\s[A-Z]\s[\w]{1,}\'[A-Z][a-z]{1,}\w)'
    first_initialdot_last = '([A-Z][a-z]{1,}\s[A-Z]\.\s[A-Z][a-z]{1,}\w)'
    first_last = '([A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\w)'
    initialdot_last = '([A-Z]\.\s[A-Z][a-z]{1,}\w)'
    regexs = [initialdot_last_suffixdot, first_initial_apostrophiclast, first_initialdot_last, first_last, initialdot_last]
    proper_names = []
    for regex in regexs:
        pattern = re.compile(regex)
        pn_list = re.findall(pattern, string)
        for pn in pn_list:
            proper_names.append(pn)
    return proper_names

#if you have strings with other proper nouns mixed in, you can create a custom list of stopwords and add that into the function
#base code for stopwords found here: http://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string

def remove_stopwords(string):
    stopwords = ['Musician','Rock','Band'] #this will eliminate "Kid Rock" from being extracted, but I think that's a good thing...
    querywords = string.split()
    resultwords  = [word for word in querywords if word not in stopwords]
    return ' '.join(resultwords)

def pn_extractor(string):
    #rough way to remove stopwords for this purpose only
    try:
        string = remove_stopwords(string)
    except:
        pass
    initialdot_last_suffixdot = '([A-Z]\.\s[A-Z][a-z]{1,}\s[A-Z][a-z]\.)'
    first_initial_apostrophiclast = '([A-Z][a-z]{1,}\s[A-Z]\s[\w]{1,}\'[A-Z][a-z]{1,}\w)'
    first_initialdot_last = '([A-Z][a-z]{1,}\s[A-Z]\.\s[A-Z][a-z]{1,}\w)'
    first_last = '([A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\w)'
    initialdot_last = '([A-Z]\.\s[A-Z][a-z]{1,}\w)'
    regexs = [initialdot_last_suffixdot, first_initial_apostrophiclast, first_initialdot_last, first_last, initialdot_last]
    proper_names = []
    try:
        for regex in regexs:
            pattern = re.compile(regex)
            pn_list = re.findall(pattern, string)
            for pn in pn_list:
                proper_names.append(pn)
    except:
        proper_names.append("None")
    return proper_names