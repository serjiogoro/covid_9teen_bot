import wikipedia
import pandas as pd

def get_wiki_table_df(page_url, match_string):
    response = requests.get(page_url)
    tables = pd.read_html(response.content)
    df = None
    for table in tables:
        df = table
        if match_string in str(df):
            break
    return df

    def get_wiki():
    url = ('https://en.wikipedia.org/wiki/') 
    df = utils.get_wiki_table_df(url, 'Locations[b]')
    df = pd.DataFrame(
        df.values[:, 1:5], 
        columns=['country', 'confirmed', 'deaths', 'recovered']
    )
    df = df[~df['country'].isna()]
    df['country'] = df['country'].apply(lambda x: utils.clean_territory_name(x))
    df.drop(df[df['country'].str.len() > 40].index, inplace=True)
    df = utils.wiki_table_df_numeric_column_clean(df, [
        'confirmed', 'deaths', 'recovered'
    ])
    df['state'] = None
    check_report(df)
    return df