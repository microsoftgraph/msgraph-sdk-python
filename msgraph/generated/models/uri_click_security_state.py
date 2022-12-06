from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UriClickSecurityState(AdditionalDataHolder, Parsable):
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
    def click_action(self,) -> Optional[str]:
        """
        Gets the clickAction property value. The clickAction property
        Returns: Optional[str]
        """
        return self._click_action
    
    @click_action.setter
    def click_action(self,value: Optional[str] = None) -> None:
        """
        Sets the clickAction property value. The clickAction property
        Args:
            value: Value to set for the clickAction property.
        """
        self._click_action = value
    
    @property
    def click_date_time(self,) -> Optional[datetime]:
        """
        Gets the clickDateTime property value. The clickDateTime property
        Returns: Optional[datetime]
        """
        return self._click_date_time
    
    @click_date_time.setter
    def click_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the clickDateTime property value. The clickDateTime property
        Args:
            value: Value to set for the clickDateTime property.
        """
        self._click_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new uriClickSecurityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The clickAction property
        self._click_action: Optional[str] = None
        # The clickDateTime property
        self._click_date_time: Optional[datetime] = None
        # The id property
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The sourceId property
        self._source_id: Optional[str] = None
        # The uriDomain property
        self._uri_domain: Optional[str] = None
        # The verdict property
        self._verdict: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UriClickSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UriClickSecurityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UriClickSecurityState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "click_action": lambda n : setattr(self, 'click_action', n.get_str_value()),
            "click_date_time": lambda n : setattr(self, 'click_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_id": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "uri_domain": lambda n : setattr(self, 'uri_domain', n.get_str_value()),
            "verdict": lambda n : setattr(self, 'verdict', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("clickAction", self.click_action)
        writer.write_datetime_value("clickDateTime", self.click_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("uriDomain", self.uri_domain)
        writer.write_str_value("verdict", self.verdict)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. The sourceId property
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. The sourceId property
        Args:
            value: Value to set for the sourceId property.
        """
        self._source_id = value
    
    @property
    def uri_domain(self,) -> Optional[str]:
        """
        Gets the uriDomain property value. The uriDomain property
        Returns: Optional[str]
        """
        return self._uri_domain
    
    @uri_domain.setter
    def uri_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the uriDomain property value. The uriDomain property
        Args:
            value: Value to set for the uriDomain property.
        """
        self._uri_domain = value
    
    @property
    def verdict(self,) -> Optional[str]:
        """
        Gets the verdict property value. The verdict property
        Returns: Optional[str]
        """
        return self._verdict
    
    @verdict.setter
    def verdict(self,value: Optional[str] = None) -> None:
        """
        Sets the verdict property value. The verdict property
        Args:
            value: Value to set for the verdict property.
        """
        self._verdict = value
    

