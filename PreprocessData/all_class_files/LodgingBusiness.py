from PreprocessData.all_class_files.LocalBusiness import LocalBusiness
import global_data


class LodgingBusiness(LocalBusiness):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, aggregateRating=None, alumni=None, areaServed=None, award=None, brand=None, contactPoint=None, department=None, dissolutionDate=None, duns=None, email=None, employee=None, event=None, faxNumber=None, founder=None, foundingDate=None, foundingLocation=None, funder=None, globalLocationNumber=None, hasOfferCatalog=None, hasPOS=None, isicV4=None, legalName=None, leiCode=None, location=None, logo=None, makesOffer=None, member=None, memberOf=None, naics=None, numberOfEmployees=None, owns=None, parentOrganization=None, publishingPrinciples=None, review=None, seeks=None, sponsor=None, subOrganization=None, taxID=None, telephone=None, vatID=None, additionalProperty=None, amenityFeature=None, branchCode=None, containedInPlace=None, containsPlace=None, geo=None, hasMap=None, isAccessibleForFree=None, maximumAttendeeCapacity=None, openingHoursSpecification=None, photo=None, publicAccess=None, smokingAllowed=None, specialOpeningHoursSpecification=None, currenciesAccepted=None, openingHours=None, paymentAccepted=None, priceRange=None, audience=None, availableLanguage=None, checkinTime=None, checkoutTime=None, petsAllowed=None, starRating=None):
        LocalBusiness.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, address, aggregateRating, alumni, areaServed, award, brand, contactPoint, department, dissolutionDate, duns, email, employee, event, faxNumber, founder, foundingDate, foundingLocation, funder, globalLocationNumber, hasOfferCatalog, hasPOS, isicV4, legalName, leiCode, location, logo, makesOffer, member, memberOf, naics, numberOfEmployees, owns, parentOrganization, publishingPrinciples, review, seeks, sponsor, subOrganization, taxID, telephone, vatID, additionalProperty, amenityFeature, branchCode, containedInPlace, containsPlace, geo, hasMap, isAccessibleForFree, maximumAttendeeCapacity, openingHoursSpecification, photo, publicAccess, smokingAllowed, specialOpeningHoursSpecification, currenciesAccepted, openingHours, paymentAccepted, priceRange)
        self.amenityFeature = amenityFeature
        self.audience = audience
        self.availableLanguage = availableLanguage
        self.checkinTime = checkinTime
        self.checkoutTime = checkoutTime
        self.petsAllowed = petsAllowed
        self.starRating = starRating

    def set_amenityFeature(self, amenityFeature):
        self.amenityFeature = amenityFeature

    def get_amenityFeature(self):
        return self.amenityFeature

    def set_audience(self, audience):
        self.audience = audience

    def get_audience(self):
        return self.audience

    def set_availableLanguage(self, availableLanguage):
        self.availableLanguage = availableLanguage

    def get_availableLanguage(self):
        return self.availableLanguage

    def set_checkinTime(self, checkinTime):
        self.checkinTime = checkinTime

    def get_checkinTime(self):
        return self.checkinTime

    def set_checkoutTime(self, checkoutTime):
        self.checkoutTime = checkoutTime

    def get_checkoutTime(self):
        return self.checkoutTime

    def set_petsAllowed(self, petsAllowed):
        self.petsAllowed = petsAllowed

    def get_petsAllowed(self):
        return self.petsAllowed

    def set_starRating(self, starRating):
        self.starRating = starRating

    def get_starRating(self):
        return self.starRating


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
