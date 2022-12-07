from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_flow_type = lazy_import('msgraph.generated.models.user_flow_type')

class IdentityUserFlow(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new identityUserFlow and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The userFlowType property
        self._user_flow_type: Optional[user_flow_type.UserFlowType] = None
        # The userFlowTypeVersion property
        self._user_flow_type_version: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityUserFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_flow_type": lambda n : setattr(self, 'user_flow_type', n.get_enum_value(user_flow_type.UserFlowType)),
            "user_flow_type_version": lambda n : setattr(self, 'user_flow_type_version', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("userFlowType", self.user_flow_type)
        writer.write_float_value("userFlowTypeVersion", self.user_flow_type_version)
    
    @property
    def user_flow_type(self,) -> Optional[user_flow_type.UserFlowType]:
        """
        Gets the userFlowType property value. The userFlowType property
        Returns: Optional[user_flow_type.UserFlowType]
        """
        return self._user_flow_type
    
    @user_flow_type.setter
    def user_flow_type(self,value: Optional[user_flow_type.UserFlowType] = None) -> None:
        """
        Sets the userFlowType property value. The userFlowType property
        Args:
            value: Value to set for the userFlowType property.
        """
        self._user_flow_type = value
    
    @property
    def user_flow_type_version(self,) -> Optional[float]:
        """
        Gets the userFlowTypeVersion property value. The userFlowTypeVersion property
        Returns: Optional[float]
        """
        return self._user_flow_type_version
    
    @user_flow_type_version.setter
    def user_flow_type_version(self,value: Optional[float] = None) -> None:
        """
        Sets the userFlowTypeVersion property value. The userFlowTypeVersion property
        Args:
            value: Value to set for the userFlowTypeVersion property.
        """
        self._user_flow_type_version = value
    

