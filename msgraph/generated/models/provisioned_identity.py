from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

details_info = lazy_import('msgraph.generated.models.details_info')
identity = lazy_import('msgraph.generated.models.identity')

class ProvisionedIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new ProvisionedIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.provisionedIdentity"
        # Details of the identity.
        self._details: Optional[details_info.DetailsInfo] = None
        # Type of identity that has been provisioned, such as 'user' or 'group'.
        self._identity_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisionedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionedIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisionedIdentity()
    
    @property
    def details(self,) -> Optional[details_info.DetailsInfo]:
        """
        Gets the details property value. Details of the identity.
        Returns: Optional[details_info.DetailsInfo]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[details_info.DetailsInfo] = None) -> None:
        """
        Sets the details property value. Details of the identity.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(details_info.DetailsInfo)),
            "identity_type": lambda n : setattr(self, 'identity_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_type(self,) -> Optional[str]:
        """
        Gets the identityType property value. Type of identity that has been provisioned, such as 'user' or 'group'.
        Returns: Optional[str]
        """
        return self._identity_type
    
    @identity_type.setter
    def identity_type(self,value: Optional[str] = None) -> None:
        """
        Sets the identityType property value. Type of identity that has been provisioned, such as 'user' or 'group'.
        Args:
            value: Value to set for the identityType property.
        """
        self._identity_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("details", self.details)
        writer.write_str_value("identityType", self.identity_type)
    

