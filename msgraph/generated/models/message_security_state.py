from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MessageSecurityState(AdditionalDataHolder, Parsable):
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
    def connecting_i_p(self,) -> Optional[str]:
        """
        Gets the connectingIP property value. The connectingIP property
        Returns: Optional[str]
        """
        return self._connecting_i_p
    
    @connecting_i_p.setter
    def connecting_i_p(self,value: Optional[str] = None) -> None:
        """
        Sets the connectingIP property value. The connectingIP property
        Args:
            value: Value to set for the connectingIP property.
        """
        self._connecting_i_p = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new messageSecurityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The connectingIP property
        self._connecting_i_p: Optional[str] = None
        # The deliveryAction property
        self._delivery_action: Optional[str] = None
        # The deliveryLocation property
        self._delivery_location: Optional[str] = None
        # The directionality property
        self._directionality: Optional[str] = None
        # The internetMessageId property
        self._internet_message_id: Optional[str] = None
        # The messageFingerprint property
        self._message_fingerprint: Optional[str] = None
        # The messageReceivedDateTime property
        self._message_received_date_time: Optional[datetime] = None
        # The messageSubject property
        self._message_subject: Optional[str] = None
        # The networkMessageId property
        self._network_message_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageSecurityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageSecurityState()
    
    @property
    def delivery_action(self,) -> Optional[str]:
        """
        Gets the deliveryAction property value. The deliveryAction property
        Returns: Optional[str]
        """
        return self._delivery_action
    
    @delivery_action.setter
    def delivery_action(self,value: Optional[str] = None) -> None:
        """
        Sets the deliveryAction property value. The deliveryAction property
        Args:
            value: Value to set for the deliveryAction property.
        """
        self._delivery_action = value
    
    @property
    def delivery_location(self,) -> Optional[str]:
        """
        Gets the deliveryLocation property value. The deliveryLocation property
        Returns: Optional[str]
        """
        return self._delivery_location
    
    @delivery_location.setter
    def delivery_location(self,value: Optional[str] = None) -> None:
        """
        Sets the deliveryLocation property value. The deliveryLocation property
        Args:
            value: Value to set for the deliveryLocation property.
        """
        self._delivery_location = value
    
    @property
    def directionality(self,) -> Optional[str]:
        """
        Gets the directionality property value. The directionality property
        Returns: Optional[str]
        """
        return self._directionality
    
    @directionality.setter
    def directionality(self,value: Optional[str] = None) -> None:
        """
        Sets the directionality property value. The directionality property
        Args:
            value: Value to set for the directionality property.
        """
        self._directionality = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connecting_i_p": lambda n : setattr(self, 'connecting_i_p', n.get_str_value()),
            "delivery_action": lambda n : setattr(self, 'delivery_action', n.get_str_value()),
            "delivery_location": lambda n : setattr(self, 'delivery_location', n.get_str_value()),
            "directionality": lambda n : setattr(self, 'directionality', n.get_str_value()),
            "internet_message_id": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "message_fingerprint": lambda n : setattr(self, 'message_fingerprint', n.get_str_value()),
            "message_received_date_time": lambda n : setattr(self, 'message_received_date_time', n.get_datetime_value()),
            "message_subject": lambda n : setattr(self, 'message_subject', n.get_str_value()),
            "network_message_id": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def internet_message_id(self,) -> Optional[str]:
        """
        Gets the internetMessageId property value. The internetMessageId property
        Returns: Optional[str]
        """
        return self._internet_message_id
    
    @internet_message_id.setter
    def internet_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the internetMessageId property value. The internetMessageId property
        Args:
            value: Value to set for the internetMessageId property.
        """
        self._internet_message_id = value
    
    @property
    def message_fingerprint(self,) -> Optional[str]:
        """
        Gets the messageFingerprint property value. The messageFingerprint property
        Returns: Optional[str]
        """
        return self._message_fingerprint
    
    @message_fingerprint.setter
    def message_fingerprint(self,value: Optional[str] = None) -> None:
        """
        Sets the messageFingerprint property value. The messageFingerprint property
        Args:
            value: Value to set for the messageFingerprint property.
        """
        self._message_fingerprint = value
    
    @property
    def message_received_date_time(self,) -> Optional[datetime]:
        """
        Gets the messageReceivedDateTime property value. The messageReceivedDateTime property
        Returns: Optional[datetime]
        """
        return self._message_received_date_time
    
    @message_received_date_time.setter
    def message_received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the messageReceivedDateTime property value. The messageReceivedDateTime property
        Args:
            value: Value to set for the messageReceivedDateTime property.
        """
        self._message_received_date_time = value
    
    @property
    def message_subject(self,) -> Optional[str]:
        """
        Gets the messageSubject property value. The messageSubject property
        Returns: Optional[str]
        """
        return self._message_subject
    
    @message_subject.setter
    def message_subject(self,value: Optional[str] = None) -> None:
        """
        Sets the messageSubject property value. The messageSubject property
        Args:
            value: Value to set for the messageSubject property.
        """
        self._message_subject = value
    
    @property
    def network_message_id(self,) -> Optional[str]:
        """
        Gets the networkMessageId property value. The networkMessageId property
        Returns: Optional[str]
        """
        return self._network_message_id
    
    @network_message_id.setter
    def network_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the networkMessageId property value. The networkMessageId property
        Args:
            value: Value to set for the networkMessageId property.
        """
        self._network_message_id = value
    
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
        writer.write_str_value("connectingIP", self.connecting_i_p)
        writer.write_str_value("deliveryAction", self.delivery_action)
        writer.write_str_value("deliveryLocation", self.delivery_location)
        writer.write_str_value("directionality", self.directionality)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_str_value("messageFingerprint", self.message_fingerprint)
        writer.write_datetime_value("messageReceivedDateTime", self.message_received_date_time)
        writer.write_str_value("messageSubject", self.message_subject)
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

