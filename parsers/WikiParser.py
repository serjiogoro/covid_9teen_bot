import wikipediaapi

def get_wiki_covid():
    covid = wikipediaapi.Wikipedia('ru')
    page_py = covid.page("Пандемия_COVID-19")
    return {'title':page_py.title, 'description': page_py.text, 'url':page_py.canonicalurl}

#wiki = get_wiki_covid()
#print (wiki['title'])