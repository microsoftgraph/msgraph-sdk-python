from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class InnerError(AdditionalDataHolder, Parsable):
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
    def client_request_id(self,) -> Optional[str]:
        """
        Gets the client-request-id property value. Client request Id as sent by the client application.
        Returns: Optional[str]
        """
        return self._client_request_id
    
    @client_request_id.setter
    def client_request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the client-request-id property value. Client request Id as sent by the client application.
        Args:
            value: Value to set for the clientRequestId property.
        """
        self._client_request_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new InnerError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Client request Id as sent by the client application.
        self._client_request_id: Optional[str] = None
        # Date when the error occured.
        self._date: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Request Id as tracked internally by the service
        self._request_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InnerError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InnerError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InnerError()
    
    @property
    def date(self,) -> Optional[datetime]:
        """
        Gets the date property value. Date when the error occured.
        Returns: Optional[datetime]
        """
        return self._date
    
    @date.setter
    def date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the date property value. Date when the error occured.
        Args:
            value: Value to set for the Date property.
        """
        self._date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client-request-id": lambda n : setattr(self, 'client_request_id', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "request-id": lambda n : setattr(self, 'request_id', n.get_str_value()),
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
    
    @property
    def request_id(self,) -> Optional[str]:
        """
        Gets the request-id property value. Request Id as tracked internally by the service
        Returns: Optional[str]
        """
        return self._request_id
    
    @request_id.setter
    def request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the request-id property value. Request Id as tracked internally by the service
        Args:
            value: Value to set for the requestId property.
        """
        self._request_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("client-request-id", self.client_request_id)
        writer.write_datetime_value("Date", self.date)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("request-id", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

