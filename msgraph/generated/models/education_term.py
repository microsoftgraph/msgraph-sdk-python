from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EducationTerm(AdditionalDataHolder, Parsable):
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
        Instantiates a new educationTerm and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Display name of the term.
        self._display_name: Optional[str] = None
        # End of the term.
        self._end_date: Optional[Date] = None
        # ID of term in the syncing system.
        self._external_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Start of the term.
        self._start_date: Optional[Date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationTerm:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationTerm
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationTerm()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the term.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the term.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_date(self,) -> Optional[Date]:
        """
        Gets the endDate property value. End of the term.
        Returns: Optional[Date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the endDate property value. End of the term.
        Args:
            value: Value to set for the endDate property.
        """
        self._end_date = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. ID of term in the syncing system.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. ID of term in the syncing system.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date": lambda n : setattr(self, 'end_date', n.get_object_value(Date)),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date": lambda n : setattr(self, 'start_date', n.get_object_value(Date)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDate", self.end_date)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date(self,) -> Optional[Date]:
        """
        Gets the startDate property value. Start of the term.
        Returns: Optional[Date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the startDate property value. Start of the term.
        Args:
            value: Value to set for the startDate property.
        """
        self._start_date = value
    

