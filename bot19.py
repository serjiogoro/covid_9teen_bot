import wikipedia

# print wikipedia.summary ("Wikipedia")


def get_wiki_covid(covid19):
    covid = wikipedia.page("Covid-19 Pandemic")
    return {'title': covid.title, 'description': covid.content, 'url':covid.url}