import pandas as pd

df = pd.read_csv('/Users/daveweimer/Desktop/WFH/BlackBoston/2020-08-18-Test2.csv',encoding='utf-8-sig')

template_columns = ['NAME','TAB_NAME','SHORT_DESC','DESC1','DESC2','DESC3','DESC4','DESC5','WEBSITE','PIC_URL','THUMB_URL','LAT','LONG']

new_df = pd.DataFrame(columns=template_columns)
bib = {'Grover and da Silva' : 'Kathryn Grover and Janine V. da Silva, "Historic Resource Study: Boston African American National Historic Site, 31 December 2002." Discover Underground Railroad History. National Parks Service.',
       'Wikipedia' : 'Wikipedia',
       'BOAF' : 'Boston African American National Historic Site',
       'Mass Moments' : 'Mass Moments',
       'CCP' : 'Colored Conventions Project',
       'Sidbury' : 'James Sidbury, Becoming African in America: Race and Nation in the Early Black Atlantic, 1760-1830. Oxford University Press, 2007.',
       'AME Zion Church website' : 'Columbus Avenue AME Zion Church website',
       'Roses' : 'Lorraine Elena Roses, Black Bostonians and the Politics of Culture, 1920-1940. University of Massachusetts Press, 2017.',
       'Stimpson\'s Boston Directory, 1836' : 'Charles Stimpson, Jr. Stimpson\'s Boston Directory, 1836.',
       'BADAA' : 'Boston Athenæum Directory of African Americans in Boston, 1820-1865 ',
       'AAAB' : 'African Americans in Antebellum Boston',
       'Carretta' : 'Vincent Carretta, Phillis Wheatley: Biography of a Genius in Bondage. University of Georgia Press, 2011.',
       'CNA' : 'Colonial North American at Harvard Library'}

def format_link(url, word, n):
    l = '<a href=\\"' + str(url) + '\\">' + word + " " + str(n) + "</a><br>"
    return l

def get_name(l, f):
    if pd.isna(l):
        return str(f)
    else:
        if pd.isna(f):
            return str(l)
        else:
            return str(f) + ' ' + str(l)

def make_url(records):
    if pd.isna(records):
        return ""
    else:
        records = str(records)
        mmsids = records.split("; ")
        urls = []
        for mmsid in mmsids:
            if "; " in mmsid:
                mmsid = mmsid.replace("; ", "")
            urls.append('http://id.lib.harvard.edu/alma/' + str(mmsid) + '/catalog')
        return_text = '<p>Records in HOLLIS include: '
        counter = 1
        for url in urls:
            l = format_link(url,"Record",counter)
            counter += 1
            return_text = return_text + l
        return return_text + "</p><br>"

def make_digs(records):
    if pd.isna(records):
        return ""
    else:
        records = str(records)
        urls = records.split("; ")
        return_text = '<p>Digital objects include: '
        counter = 1
        for url in urls:
            l = format_link(url, "Digital Object", counter)
            counter += 1
            return_text = return_text + l
        return return_text + "</p><br>"

def bib_entry(ids, bib):
    if pd.isna(ids):
        return ""
    else:
        ids = str(ids)
        ids_list = ids.split("; ")
        return_text = '<p>Sources: '
        for id in ids_list:
            return_text = return_text + str(bib[id]) + '. '
        return return_text + "</p><br>"

def make_notes(records):
    if pd.isna(records):
        return ""
    else:
        notes = "<p>Notes: " + str(records) + "</p><br>"
        return notes

def get_date(s, e):
    if pd.isna(s) and pd.isna(e):
        return "No date available.<br>"
    else:
        if pd.isna(s):
            e = int(e)
            return "in " + str(e) + ".<br>"
        else:
            if pd.isna(e):
                s = int(s)
                return "since " + str(s) + ".<br>"
            else:
                s = int(s)
                e = int(e)
                return "from " + str(s) + ' to ' + str(e) + ".<br>"

new_df['NAME'] = [get_name(x,y) for x, y in zip(df['Last_Name/Organization_Name/Title'], df['First_Names/Author'])]
new_df['LAT'] = df['Lat']
new_df['LONG'] = df['Long']
new_df['TAB_NAME'] = df['Type']
new_df['SHORT_DESC'] = [str(a) + " " + str(b) + " here " + get_date(c, d) + '\n' + make_url(e) + make_digs(f) +
                        make_notes(g) + bib_entry(h, bib) for a, b, c, d, e, f, g, h in
                        zip(new_df['NAME'], df['Action'], df['Start_Year_for_Location'], df['End_Year_for_Location'],
                            df['Records_(semi-colon_separated)'], df['Digital_Assets_(semi-colon_separated)'],
                            df['Notes'],df['Source_(semi-colon_separated)'])]

new_df.to_csv('/Users/daveweimer/Desktop/WFH/BlackBoston/2020-08-23-TestOutput-4.csv')
