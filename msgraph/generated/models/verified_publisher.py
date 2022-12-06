from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VerifiedPublisher(AdditionalDataHolder, Parsable):
    @property
    def added_date_time(self,) -> Optional[datetime]:
        """
        Gets the addedDateTime property value. The timestamp when the verified publisher was first added or most recently updated.
        Returns: Optional[datetime]
        """
        return self._added_date_time
    
    @added_date_time.setter
    def added_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the addedDateTime property value. The timestamp when the verified publisher was first added or most recently updated.
        Args:
            value: Value to set for the addedDateTime property.
        """
        self._added_date_time = value
    
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
        Instantiates a new verifiedPublisher and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The timestamp when the verified publisher was first added or most recently updated.
        self._added_date_time: Optional[datetime] = None
        # The verified publisher name from the app publisher's Partner Center account.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the verified publisher from the app publisher's Partner Center account.
        self._verified_publisher_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiedPublisher:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedPublisher
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiedPublisher()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The verified publisher name from the app publisher's Partner Center account.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The verified publisher name from the app publisher's Partner Center account.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "added_date_time": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "verified_publisher_id": lambda n : setattr(self, 'verified_publisher_id', n.get_str_value()),
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
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("verifiedPublisherId", self.verified_publisher_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def verified_publisher_id(self,) -> Optional[str]:
        """
        Gets the verifiedPublisherId property value. The ID of the verified publisher from the app publisher's Partner Center account.
        Returns: Optional[str]
        """
        return self._verified_publisher_id
    
    @verified_publisher_id.setter
    def verified_publisher_id(self,value: Optional[str] = None) -> None:
        """
        Sets the verifiedPublisherId property value. The ID of the verified publisher from the app publisher's Partner Center account.
        Args:
            value: Value to set for the verifiedPublisherId property.
        """
        self._verified_publisher_id = value
    

