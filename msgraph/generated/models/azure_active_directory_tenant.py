from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_source

from . import identity_source

class AzureActiveDirectoryTenant(identity_source.IdentitySource):
    def __init__(self,) -> None:
        """
        Instantiates a new AzureActiveDirectoryTenant and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.azureActiveDirectoryTenant"
        # The name of the Azure Active Directory tenant. Read only.
        self._display_name: Optional[str] = None
        # The ID of the Azure Active Directory tenant. Read only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureActiveDirectoryTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureActiveDirectoryTenant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureActiveDirectoryTenant()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the Azure Active Directory tenant. Read only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the Azure Active Directory tenant. Read only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_source

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The ID of the Azure Active Directory tenant. Read only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The ID of the Azure Active Directory tenant. Read only.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

