from PreprocessData.all_class_files.InsertAction import InsertAction
import global_data


class PrependAction(InsertAction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None, targetCollection=None, toLocation=None):
        InsertAction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, actionStatus, agent, endTime, error, instrument, location, object, participant, result, startTime, target, targetCollection, toLocation)
