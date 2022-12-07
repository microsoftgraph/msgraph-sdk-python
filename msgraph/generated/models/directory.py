from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

administrative_unit = lazy_import('msgraph.generated.models.administrative_unit')
directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')

class Directory(entity.Entity):
    @property
    def administrative_units(self,) -> Optional[List[administrative_unit.AdministrativeUnit]]:
        """
        Gets the administrativeUnits property value. Conceptual container for user and group directory objects.
        Returns: Optional[List[administrative_unit.AdministrativeUnit]]
        """
        return self._administrative_units
    
    @administrative_units.setter
    def administrative_units(self,value: Optional[List[administrative_unit.AdministrativeUnit]] = None) -> None:
        """
        Sets the administrativeUnits property value. Conceptual container for user and group directory objects.
        Args:
            value: Value to set for the administrativeUnits property.
        """
        self._administrative_units = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Directory and sets the default values.
        """
        super().__init__()
        # Conceptual container for user and group directory objects.
        self._administrative_units: Optional[List[administrative_unit.AdministrativeUnit]] = None
        # Recently deleted items. Read-only. Nullable.
        self._deleted_items: Optional[List[directory_object.DirectoryObject]] = None
        # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        self._federation_configurations: Optional[List[identity_provider_base.IdentityProviderBase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Directory()
    
    @property
    def deleted_items(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the deletedItems property value. Recently deleted items. Read-only. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._deleted_items
    
    @deleted_items.setter
    def deleted_items(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the deletedItems property value. Recently deleted items. Read-only. Nullable.
        Args:
            value: Value to set for the deletedItems property.
        """
        self._deleted_items = value
    
    @property
    def federation_configurations(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the federationConfigurations property value. Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._federation_configurations
    
    @federation_configurations.setter
    def federation_configurations(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the federationConfigurations property value. Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        Args:
            value: Value to set for the federationConfigurations property.
        """
        self._federation_configurations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "administrative_units": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(administrative_unit.AdministrativeUnit)),
            "deleted_items": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "federation_configurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
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
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
    

