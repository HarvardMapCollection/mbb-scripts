# Code to create data for Leaflet map

import pandas as pd
import urllib.request
import xmltodict
import geopandas

# import the csv data as a DataFrame
df = pd.read_csv('DATA_20200918.csv',encoding='utf-8-sig')

# Project sources stored as dict rather than as a separate csv
bib = {'Grover and da Silva' : 'Kathryn Grover and Janine V. da Silva, "Historic Resource Study: Boston African American National Historic Site, 31 December 2002." Discover Underground Railroad History. National Parks Service.',
       'Wikipedia' : 'Wikipedia.',
       'BOAF' : 'Boston African American National Historic Site.',
       'Mass Moments' : 'Mass Moments.',
       'CCP' : 'Colored Conventions Project.',
       'Sidbury' : 'James Sidbury, Becoming African in America: Race and Nation in the Early Black Atlantic, 1760-1830. Oxford University Press, 2007.',
       'AME Zion Church website' : 'Columbus Avenue AME Zion Church website.',
       'Roses' : 'Lorraine Elena Roses, Black Bostonians and the Politics of Culture, 1920-1940. University of Massachusetts Press, 2017.',
       'Stimpson\'s Boston Directory, 1836' : 'Charles Stimpson, Jr. Stimpson\'s Boston Directory, 1836.',
       'BADAA' : 'Boston Athenæum Directory of African Americans in Boston, 1820-1865.',
       'AAAB' : 'African Americans in Antebellum Boston.',
       'Carretta' : 'Vincent Carretta, Phillis Wheatley: Biography of a Genius in Bondage. University of Georgia Press, 2011.',
       'CNA' : 'Colonial North American at Harvard Library.'}

def get_title(hollis):
    xml_request = urllib.request.urlopen('http://api.lib.harvard.edu/v2/items?recordIdentifier=' + str(hollis))
    full_xml = xmltodict.parse(xml_request)
    try:
        title = full_xml['results']['items']['mods:mods']['mods:titleInfo']['mods:title']
    except TypeError:
        title = full_xml['results']['items']['mods:mods']['mods:titleInfo'][0]['mods:title']
    title = str(title)
    title = title.capitalize()
    return title

# Return a dictionary of HOLLIS numbers and urls from a dataframe column, records originally separated by semi-colons
def record_dict(records):
    if pd.isna(records):
        return ""
    else:
        records = str(records)
        mmsids = records.split(";")
        info = {}
        for mmsid in mmsids:
            if mmsid == "" or mmsid == " " or mmsid == ";":
                mmsids.remove(mmsid)
            else:
                if ";" in mmsid:
                    mmsid = mmsid.replace(";", "")
                mmsid = mmsid.strip()
                url = 'https://id.lib.harvard.edu/alma/' + str(mmsid) + '/catalog'
                title = get_title(mmsid)
                info[mmsid] = [url,title]
        return info

# Return a string of urls with with html breaks from a list of urls to digital objects separated by semi-colons
def make_digs(records):
    if pd.isna(records):
        return ""
    else:
        records = str(records)
        urls = records.split("; ")
    return ""

# return a string with an html break from a list of source abbreviations separated by semi-colons
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
                return_text = return_text + str(bib[id])
        else:
            return_text = return_text + str(bib[ids])
        return return_text


# replace the abbreviation for the sources with their full bibliographic entry
source_list = df['SOURCE'].tolist()
full_source_list = []

for s in source_list:
    full_source_list.append(bib_entry(s,bib))

df['SOURCE'] = full_source_list

# Create link text and links for up to three HOLLIS records for each row
r_list = df['RECORDS'].tolist()
title_1 = []
url_1 = []
title_2 = []
url_2 = []
title_3 = []
url_3 = []

for r in r_list:
    r_dict = record_dict(r)
    if bool(r_dict):
        mmsids = [*r_dict]
        total_keys = len(mmsids)
        title_1.append(r_dict[mmsids[0]][1])
        url_1.append(r_dict[mmsids[0]][0])
        if total_keys > 1:
            title_2.append(r_dict[mmsids[1]][1])
            url_2.append(r_dict[mmsids[1]][0])
        else:
            title_2.append("")
            url_2.append("")
        if total_keys > 2:
            title_3.append(r_dict[mmsids[2]][1])
            url_3.append(r_dict[mmsids[2]][0])
        else:
            title_3.append("")
            url_3.append("")
    else:
        title_1.append("")
        url_1.append("")
        title_2.append("")
        url_2.append("")
        title_3.append("")
        url_3.append("")


df['TITLE_1'] = title_1
df['URL_1'] = url_1
df['TITLE_2'] = title_2
df['URL_2'] = url_2
df['TITLE_3'] = title_3
df['URL_3'] = url_3

# write a new csv
df.to_csv('Leaflet_TestOutput.csv')

# write GeoJSON
gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['LONG'], df['LAT']))
gdf.to_file("Leaflet_TestOutput.geojson", driver='GeoJSON')
