from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EducationCourse(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationCourse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Unique identifier for the course.
        self._course_number: Optional[str] = None
        # Description of the course.
        self._description: Optional[str] = None
        # Name of the course.
        self._display_name: Optional[str] = None
        # ID of the course from the syncing system.
        self._external_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Subject of the course.
        self._subject: Optional[str] = None
    
    @property
    def course_number(self,) -> Optional[str]:
        """
        Gets the courseNumber property value. Unique identifier for the course.
        Returns: Optional[str]
        """
        return self._course_number
    
    @course_number.setter
    def course_number(self,value: Optional[str] = None) -> None:
        """
        Sets the courseNumber property value. Unique identifier for the course.
        Args:
            value: Value to set for the courseNumber property.
        """
        self._course_number = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationCourse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationCourse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationCourse()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the course.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the course.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the course.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the course.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. ID of the course from the syncing system.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. ID of the course from the syncing system.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "course_number": lambda n : setattr(self, 'course_number', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("courseNumber", self.course_number)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. Subject of the course.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. Subject of the course.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

