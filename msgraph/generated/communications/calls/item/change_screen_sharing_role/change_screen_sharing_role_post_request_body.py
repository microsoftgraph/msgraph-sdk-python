from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

screen_sharing_role = lazy_import('msgraph.generated.models.screen_sharing_role')

class ChangeScreenSharingRolePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the changeScreenSharingRole method.
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
        Instantiates a new changeScreenSharingRolePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The role property
        self._role: Optional[screen_sharing_role.ScreenSharingRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeScreenSharingRolePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeScreenSharingRolePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChangeScreenSharingRolePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(screen_sharing_role.ScreenSharingRole)),
        }
        return fields
    
    @property
    def role(self,) -> Optional[screen_sharing_role.ScreenSharingRole]:
        """
        Gets the role property value. The role property
        Returns: Optional[screen_sharing_role.ScreenSharingRole]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[screen_sharing_role.ScreenSharingRole] = None) -> None:
        """
        Sets the role property value. The role property
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

