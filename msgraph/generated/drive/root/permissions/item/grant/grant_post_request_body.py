from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

drive_recipient = lazy_import('msgraph.generated.models.drive_recipient')

class GrantPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the grant method.
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
        Instantiates a new grantPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The recipients property
        self._recipients: Optional[List[drive_recipient.DriveRecipient]] = None
        # The roles property
        self._roles: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GrantPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GrantPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GrantPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(drive_recipient.DriveRecipient)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def recipients(self,) -> Optional[List[drive_recipient.DriveRecipient]]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[List[drive_recipient.DriveRecipient]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[drive_recipient.DriveRecipient]] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    @property
    def roles(self,) -> Optional[List[str]]:
        """
        Gets the roles property value. The roles property
        Returns: Optional[List[str]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roles property value. The roles property
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_additional_data_value(self.additional_data)
    

