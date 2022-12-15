from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class DirectoryObjectPartnerReference(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new DirectoryObjectPartnerReference and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.directoryObjectPartnerReference"
        # Description of the object returned. Read-only.
        self._description: Optional[str] = None
        # Name of directory object being returned, like group or application. Read-only.
        self._display_name: Optional[str] = None
        # The tenant identifier for the partner tenant. Read-only.
        self._external_partner_tenant_id: Optional[Guid] = None
        # The type of the referenced object in the partner tenant. Read-only.
        self._object_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryObjectPartnerReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObjectPartnerReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryObjectPartnerReference()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the object returned. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the object returned. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of directory object being returned, like group or application. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of directory object being returned, like group or application. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_partner_tenant_id(self,) -> Optional[Guid]:
        """
        Gets the externalPartnerTenantId property value. The tenant identifier for the partner tenant. Read-only.
        Returns: Optional[Guid]
        """
        return self._external_partner_tenant_id
    
    @external_partner_tenant_id.setter
    def external_partner_tenant_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the externalPartnerTenantId property value. The tenant identifier for the partner tenant. Read-only.
        Args:
            value: Value to set for the externalPartnerTenantId property.
        """
        self._external_partner_tenant_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_partner_tenant_id": lambda n : setattr(self, 'external_partner_tenant_id', n.get_object_value(Guid)),
            "object_type": lambda n : setattr(self, 'object_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def object_type(self,) -> Optional[str]:
        """
        Gets the objectType property value. The type of the referenced object in the partner tenant. Read-only.
        Returns: Optional[str]
        """
        return self._object_type
    
    @object_type.setter
    def object_type(self,value: Optional[str] = None) -> None:
        """
        Sets the objectType property value. The type of the referenced object in the partner tenant. Read-only.
        Args:
            value: Value to set for the objectType property.
        """
        self._object_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("externalPartnerTenantId", self.external_partner_tenant_id)
        writer.write_str_value("objectType", self.object_type)
    

