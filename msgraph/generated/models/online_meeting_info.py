from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

phone = lazy_import('msgraph.generated.models.phone')

class OnlineMeetingInfo(AdditionalDataHolder, Parsable):
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
        Gets the conferenceId property value. The ID of the conference.
        Returns: Optional[str]
        """
        return self._conference_id
    
    @conference_id.setter
    def conference_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conferenceId property value. The ID of the conference.
        Args:
            value: Value to set for the conferenceId property.
        """
        self._conference_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onlineMeetingInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ID of the conference.
        self._conference_id: Optional[str] = None
        # The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.
        self._join_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # All of the phone numbers associated with this conference.
        self._phones: Optional[List[phone.Phone]] = None
        # The pre-formatted quickdial for this call.
        self._quick_dial: Optional[str] = None
        # The toll free numbers that can be used to join the conference.
        self._toll_free_numbers: Optional[List[str]] = None
        # The toll number that can be used to join the conference.
        self._toll_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnlineMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conference_id": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "join_url": lambda n : setattr(self, 'join_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(phone.Phone)),
            "quick_dial": lambda n : setattr(self, 'quick_dial', n.get_str_value()),
            "toll_free_numbers": lambda n : setattr(self, 'toll_free_numbers', n.get_collection_of_primitive_values(str)),
            "toll_number": lambda n : setattr(self, 'toll_number', n.get_str_value()),
        }
        return fields
    
    @property
    def join_url(self,) -> Optional[str]:
        """
        Gets the joinUrl property value. The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.
        Returns: Optional[str]
        """
        return self._join_url
    
    @join_url.setter
    def join_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinUrl property value. The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.
        Args:
            value: Value to set for the joinUrl property.
        """
        self._join_url = value
    
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
    
    @property
    def phones(self,) -> Optional[List[phone.Phone]]:
        """
        Gets the phones property value. All of the phone numbers associated with this conference.
        Returns: Optional[List[phone.Phone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[phone.Phone]] = None) -> None:
        """
        Sets the phones property value. All of the phone numbers associated with this conference.
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    @property
    def quick_dial(self,) -> Optional[str]:
        """
        Gets the quickDial property value. The pre-formatted quickdial for this call.
        Returns: Optional[str]
        """
        return self._quick_dial
    
    @quick_dial.setter
    def quick_dial(self,value: Optional[str] = None) -> None:
        """
        Sets the quickDial property value. The pre-formatted quickdial for this call.
        Args:
            value: Value to set for the quickDial property.
        """
        self._quick_dial = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_str_value("joinUrl", self.join_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_str_value("quickDial", self.quick_dial)
        writer.write_collection_of_primitive_values("tollFreeNumbers", self.toll_free_numbers)
        writer.write_str_value("tollNumber", self.toll_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def toll_free_numbers(self,) -> Optional[List[str]]:
        """
        Gets the tollFreeNumbers property value. The toll free numbers that can be used to join the conference.
        Returns: Optional[List[str]]
        """
        return self._toll_free_numbers
    
    @toll_free_numbers.setter
    def toll_free_numbers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tollFreeNumbers property value. The toll free numbers that can be used to join the conference.
        Args:
            value: Value to set for the tollFreeNumbers property.
        """
        self._toll_free_numbers = value
    
    @property
    def toll_number(self,) -> Optional[str]:
        """
        Gets the tollNumber property value. The toll number that can be used to join the conference.
        Returns: Optional[str]
        """
        return self._toll_number
    
    @toll_number.setter
    def toll_number(self,value: Optional[str] = None) -> None:
        """
        Sets the tollNumber property value. The toll number that can be used to join the conference.
        Args:
            value: Value to set for the tollNumber property.
        """
        self._toll_number = value
    

