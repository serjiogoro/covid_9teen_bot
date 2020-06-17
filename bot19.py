import wikipedia

# print wikipedia.summary ("Wikipedia")


def get_wiki_covid(Пандемия_Covid_19):
    covid = wikipedia.page("Пандемия_Covid_19")
    return {'title': covid.title, 'description': covid.content, 'url':covid.url}