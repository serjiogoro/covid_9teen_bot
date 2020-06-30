import wikipedia

# print wikipedia.summary ("Wikipedia")


def get_wiki_covid():
    covid = wikipedia.page("Covid-19 Pandemic")
    return {'title': covid.title, 'description': covid.content, 'url':covid.url}

print (get_wiki_covid())