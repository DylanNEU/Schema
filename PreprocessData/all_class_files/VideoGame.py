from PreprocessData.all_class_files.SoftwareApplication import SoftwareApplication
from PreprocessData.all_class_files.Game import Game
import global_data


class VideoGame(SoftwareApplication,Game):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, applicationCategory=None, applicationSubCategory=None, applicationSuite=None, availableOnDevice=None, countriesNotSupported=None, countriesSupported=None, downloadUrl=None, featureList=None, fileSize=None, installUrl=None, memoryRequirements=None, operatingSystem=None, permissions=None, processorRequirements=None, releaseNotes=None, screenshot=None, softwareAddOn=None, softwareHelp=None, softwareRequirements=None, softwareVersion=None, storageRequirements=None, supportingData=None, characterAttribute=None, gameItem=None, gameLocation=None, numberOfPlayers=None, quest=None, actor=None, cheatCode=None, director=None, gamePlatform=None, gameServer=None, gameTip=None, musicBy=None, playMode=None, trailer=None):
        SoftwareApplication.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, applicationCategory, applicationSubCategory, applicationSuite, availableOnDevice, countriesNotSupported, countriesSupported, downloadUrl, featureList, fileSize, installUrl, memoryRequirements, operatingSystem, permissions, processorRequirements, releaseNotes, screenshot, softwareAddOn, softwareHelp, softwareRequirements, softwareVersion, storageRequirements, supportingData)
        Game.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, characterAttribute, gameItem, gameLocation, numberOfPlayers, quest)
        self.actor = actor
        self.cheatCode = cheatCode
        self.director = director
        self.gamePlatform = gamePlatform
        self.gameServer = gameServer
        self.gameTip = gameTip
        self.musicBy = musicBy
        self.playMode = playMode
        self.trailer = trailer

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor

    def set_cheatCode(self, cheatCode):
        self.cheatCode = cheatCode

    def get_cheatCode(self):
        return self.cheatCode

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_gamePlatform(self, gamePlatform):
        self.gamePlatform = gamePlatform

    def get_gamePlatform(self):
        return self.gamePlatform

    def set_gameServer(self, gameServer):
        self.gameServer = gameServer

    def get_gameServer(self):
        return self.gameServer

    def set_gameTip(self, gameTip):
        self.gameTip = gameTip

    def get_gameTip(self):
        return self.gameTip

    def set_musicBy(self, musicBy):
        self.musicBy = musicBy

    def get_musicBy(self):
        return self.musicBy

    def set_playMode(self, playMode):
        self.playMode = playMode

    def get_playMode(self):
        return self.playMode

    def set_trailer(self, trailer):
        self.trailer = trailer

    def get_trailer(self):
        return self.trailer


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
