from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_type = lazy_import('msgraph.generated.models.external_connectors.identity_type')

class Identity(entity.Entity):
    """
    Provides operations to manage the collection of externalConnection entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new identity and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type of identity. Possible values are: user or group for Azure AD identities and externalgroup for groups in an external system.
        self._type: Optional[identity_type.IdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Identity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(identity_type.IdentityType)),
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
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[identity_type.IdentityType]:
        """
        Gets the type property value. The type of identity. Possible values are: user or group for Azure AD identities and externalgroup for groups in an external system.
        Returns: Optional[identity_type.IdentityType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[identity_type.IdentityType] = None) -> None:
        """
        Sets the type property value. The type of identity. Possible values are: user or group for Azure AD identities and externalgroup for groups in an external system.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

