from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ValidatePropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the validateProperties method.
    """
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
        Instantiates a new validatePropertiesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The displayName property
        self._display_name: Optional[str] = None
        # The entityType property
        self._entity_type: Optional[str] = None
        # The mailNickname property
        self._mail_nickname: Optional[str] = None
        # The onBehalfOfUserId property
        self._on_behalf_of_user_id: Optional[Guid] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidatePropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidatePropertiesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidatePropertiesPostRequestBody()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def entity_type(self,) -> Optional[str]:
        """
        Gets the entityType property value. The entityType property
        Returns: Optional[str]
        """
        return self._entity_type
    
    @entity_type.setter
    def entity_type(self,value: Optional[str] = None) -> None:
        """
        Sets the entityType property value. The entityType property
        Args:
            value: Value to set for the entityType property.
        """
        self._entity_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "entity_type": lambda n : setattr(self, 'entity_type', n.get_str_value()),
            "mail_nickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "on_behalf_of_user_id": lambda n : setattr(self, 'on_behalf_of_user_id', n.get_object_value(Guid)),
        }
        return fields
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mailNickname property
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mailNickname property
        Args:
            value: Value to set for the mailNickname property.
        """
        self._mail_nickname = value
    
    @property
    def on_behalf_of_user_id(self,) -> Optional[Guid]:
        """
        Gets the onBehalfOfUserId property value. The onBehalfOfUserId property
        Returns: Optional[Guid]
        """
        return self._on_behalf_of_user_id
    
    @on_behalf_of_user_id.setter
    def on_behalf_of_user_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the onBehalfOfUserId property value. The onBehalfOfUserId property
        Args:
            value: Value to set for the onBehalfOfUserId property.
        """
        self._on_behalf_of_user_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("entityType", self.entity_type)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_object_value("onBehalfOfUserId", self.on_behalf_of_user_id)
        writer.write_additional_data_value(self.additional_data)
    

