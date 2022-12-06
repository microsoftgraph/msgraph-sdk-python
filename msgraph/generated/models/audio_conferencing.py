from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AudioConferencing(AdditionalDataHolder, Parsable):
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
    
    @property
    def conference_id(self,) -> Optional[str]:
        """
        Gets the conferenceId property value. The conference id of the online meeting.
        Returns: Optional[str]
        """
        return self._conference_id
    
    @conference_id.setter
    def conference_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conferenceId property value. The conference id of the online meeting.
        Args:
            value: Value to set for the conferenceId property.
        """
        self._conference_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new audioConferencing and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The conference id of the online meeting.
        self._conference_id: Optional[str] = None
        # A URL to the externally-accessible web page that contains dial-in information.
        self._dialin_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tollFreeNumber property
        self._toll_free_number: Optional[str] = None
        # List of toll-free numbers that are displayed in the meeting invite.
        self._toll_free_numbers: Optional[List[str]] = None
        # The tollNumber property
        self._toll_number: Optional[str] = None
        # List of toll numbers that are displayed in the meeting invite.
        self._toll_numbers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AudioConferencing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AudioConferencing
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AudioConferencing()
    
    @property
    def dialin_url(self,) -> Optional[str]:
        """
        Gets the dialinUrl property value. A URL to the externally-accessible web page that contains dial-in information.
        Returns: Optional[str]
        """
        return self._dialin_url
    
    @dialin_url.setter
    def dialin_url(self,value: Optional[str] = None) -> None:
        """
        Sets the dialinUrl property value. A URL to the externally-accessible web page that contains dial-in information.
        Args:
            value: Value to set for the dialinUrl property.
        """
        self._dialin_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conference_id": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "dialin_url": lambda n : setattr(self, 'dialin_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "toll_free_number": lambda n : setattr(self, 'toll_free_number', n.get_str_value()),
            "toll_free_numbers": lambda n : setattr(self, 'toll_free_numbers', n.get_collection_of_primitive_values(str)),
            "toll_number": lambda n : setattr(self, 'toll_number', n.get_str_value()),
            "toll_numbers": lambda n : setattr(self, 'toll_numbers', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_str_value("dialinUrl", self.dialin_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tollFreeNumber", self.toll_free_number)
        writer.write_collection_of_primitive_values("tollFreeNumbers", self.toll_free_numbers)
        writer.write_str_value("tollNumber", self.toll_number)
        writer.write_collection_of_primitive_values("tollNumbers", self.toll_numbers)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def toll_free_number(self,) -> Optional[str]:
        """
        Gets the tollFreeNumber property value. The tollFreeNumber property
        Returns: Optional[str]
        """
        return self._toll_free_number
    
    @toll_free_number.setter
    def toll_free_number(self,value: Optional[str] = None) -> None:
        """
        Sets the tollFreeNumber property value. The tollFreeNumber property
        Args:
            value: Value to set for the tollFreeNumber property.
        """
        self._toll_free_number = value
    
    @property
    def toll_free_numbers(self,) -> Optional[List[str]]:
        """
        Gets the tollFreeNumbers property value. List of toll-free numbers that are displayed in the meeting invite.
        Returns: Optional[List[str]]
        """
        return self._toll_free_numbers
    
    @toll_free_numbers.setter
    def toll_free_numbers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tollFreeNumbers property value. List of toll-free numbers that are displayed in the meeting invite.
        Args:
            value: Value to set for the tollFreeNumbers property.
        """
        self._toll_free_numbers = value
    
    @property
    def toll_number(self,) -> Optional[str]:
        """
        Gets the tollNumber property value. The tollNumber property
        Returns: Optional[str]
        """
        return self._toll_number
    
    @toll_number.setter
    def toll_number(self,value: Optional[str] = None) -> None:
        """
        Sets the tollNumber property value. The tollNumber property
        Args:
            value: Value to set for the tollNumber property.
        """
        self._toll_number = value
    
    @property
    def toll_numbers(self,) -> Optional[List[str]]:
        """
        Gets the tollNumbers property value. List of toll numbers that are displayed in the meeting invite.
        Returns: Optional[List[str]]
        """
        return self._toll_numbers
    
    @toll_numbers.setter
    def toll_numbers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tollNumbers property value. List of toll numbers that are displayed in the meeting invite.
        Args:
            value: Value to set for the tollNumbers property.
        """
        self._toll_numbers = value
    

