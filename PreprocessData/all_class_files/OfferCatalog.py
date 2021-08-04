from PreprocessData.all_class_files.ItemList import ItemList
import global_data


class OfferCatalog(ItemList):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, itemListElement=None, itemListOrder=None, numberOfItems=None):
        ItemList.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, itemListElement, itemListOrder, numberOfItems)
