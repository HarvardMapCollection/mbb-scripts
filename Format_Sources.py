import pandas as pd

#import the csv data as a DataFrame
df = pd.read_csv('DATA_20200918.csv',encoding='utf-8-sig')

#Project sources stored as dict rather than as a separate csv
bib = {'Grover and da Silva' : 'Kathryn Grover and Janine V. da Silva, "Historic Resource Study: Boston African American National Historic Site, 31 December 2002." Discover Underground Railroad History. National Parks Service.',
       'Wikipedia' : 'Wikipedia',
       'BOAF' : 'Boston African American National Historic Site',
       'Mass Moments' : 'Mass Moments',
       'CCP' : 'Colored Conventions Project',
       'Sidbury' : 'James Sidbury, Becoming African in America: Race and Nation in the Early Black Atlantic, 1760-1830. Oxford University Press, 2007.',
       'AME Zion Church website' : 'Columbus Avenue AME Zion Church website',
       'Roses' : 'Lorraine Elena Roses, Black Bostonians and the Politics of Culture, 1920-1940. University of Massachusetts Press, 2017.',
       'Stimpson\'s Boston Directory, 1836' : 'Charles Stimpson, Jr. Stimpson\'s Boston Directory, 1836.',
       'BADAA' : 'Boston Athenæum Directory of African Americans in Boston, 1820-1865.',
       'AAAB' : 'African Americans in Antebellum Boston',
       'Carretta' : 'Vincent Carretta, Phillis Wheatley: Biography of a Genius in Bondage. University of Georgia Press, 2011.',
       'CNA' : 'Colonial North American at Harvard Library.'}

#return a string with an html break from a list of source abbreviations separated by semi-colons
def bib_entry(ids, bib):
    if pd.isna(ids):
        return ""
    else:
        ids = str(ids)
        return_text = ''
        if ";" in ids:
            ids_list = ids.split(";")
            for id in ids_list:
                id = id.strip()
                return_text = return_text + str(bib[id]) + ' '
        else:
            return_text = return_text + str(bib[ids]) + ' '
        return return_text

s_list = df['SOURCE'].tolist()
o_list = []



for s in s_list:
    o_list.append(bib_entry(s,bib))

df['SOURCE_PRETTY'] = o_list

df.to_csv('20200918_SOURCES.csv')
