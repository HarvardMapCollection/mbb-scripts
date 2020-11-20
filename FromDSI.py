#https://gitlab.com/hldsi/WikiMedia_Currency_Collection/-/blob/master/irmafrat/harvard_item_class_xml.py

def get_title(self):
    return self.api_dom.find("mods:titleinfo").string.replace(", ", "_")

def get_embbed_urls(self):
    urls= {}
    try:
        hollis_images = self.api_dom.find("mods:relateditem", {"othertype":"HOLLIS Images record"}).find("mods:url").string
        urls.update({"Harvard Hollis Images": hollis_images})
    except:
        print ("No HOLLIS Image record found")
    urls_context = self.api_dom.findAll("mods:url",{"access":"object in context"})
    for mods_url in urls_context:
        try:
            url = mods_url.string
            key = mods_url.attrs["displaylabel"]
            if "curiosity" in url:
                key = "CURIOSity - " + key
            urls.update({key:url})
        except:
            print("No displaylabel found")
    return urls