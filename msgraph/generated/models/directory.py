from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import administrative_unit, attribute_set, custom_security_attribute_definition, directory_object, entity, identity_provider_base, on_premises_directory_synchronization

from . import entity

class Directory(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Directory and sets the default values.
        """
        super().__init__()
        # Conceptual container for user and group directory objects.
        self._administrative_units: Optional[List[administrative_unit.AdministrativeUnit]] = None
        # The attributeSets property
        self._attribute_sets: Optional[List[attribute_set.AttributeSet]] = None
        # The customSecurityAttributeDefinitions property
        self._custom_security_attribute_definitions: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None
        # Recently deleted items. Read-only. Nullable.
        self._deleted_items: Optional[List[directory_object.DirectoryObject]] = None
        # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        self._federation_configurations: Optional[List[identity_provider_base.IdentityProviderBase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A container for on-premises directory synchronization functionalities that are available for the organization.
        self._on_premises_synchronization: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None
    
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
            value: Value to set for the administrative_units property.
        """
        self._administrative_units = value
    
    @property
    def attribute_sets(self,) -> Optional[List[attribute_set.AttributeSet]]:
        """
        Gets the attributeSets property value. The attributeSets property
        Returns: Optional[List[attribute_set.AttributeSet]]
        """
        return self._attribute_sets
    
    @attribute_sets.setter
    def attribute_sets(self,value: Optional[List[attribute_set.AttributeSet]] = None) -> None:
        """
        Sets the attributeSets property value. The attributeSets property
        Args:
            value: Value to set for the attribute_sets property.
        """
        self._attribute_sets = value
    
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
    def custom_security_attribute_definitions(self,) -> Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]]:
        """
        Gets the customSecurityAttributeDefinitions property value. The customSecurityAttributeDefinitions property
        Returns: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]]
        """
        return self._custom_security_attribute_definitions
    
    @custom_security_attribute_definitions.setter
    def custom_security_attribute_definitions(self,value: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None) -> None:
        """
        Sets the customSecurityAttributeDefinitions property value. The customSecurityAttributeDefinitions property
        Args:
            value: Value to set for the custom_security_attribute_definitions property.
        """
        self._custom_security_attribute_definitions = value
    
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
            value: Value to set for the deleted_items property.
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
            value: Value to set for the federation_configurations property.
        """
        self._federation_configurations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import administrative_unit, attribute_set, custom_security_attribute_definition, directory_object, entity, identity_provider_base, on_premises_directory_synchronization

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(administrative_unit.AdministrativeUnit)),
            "attributeSets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(attribute_set.AttributeSet)),
            "customSecurityAttributeDefinitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(custom_security_attribute_definition.CustomSecurityAttributeDefinition)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "federationConfigurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "onPremisesSynchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(on_premises_directory_synchronization.OnPremisesDirectorySynchronization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def on_premises_synchronization(self,) -> Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]]:
        """
        Gets the onPremisesSynchronization property value. A container for on-premises directory synchronization functionalities that are available for the organization.
        Returns: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]]
        """
        return self._on_premises_synchronization
    
    @on_premises_synchronization.setter
    def on_premises_synchronization(self,value: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None) -> None:
        """
        Sets the onPremisesSynchronization property value. A container for on-premises directory synchronization functionalities that are available for the organization.
        Args:
            value: Value to set for the on_premises_synchronization property.
        """
        self._on_premises_synchronization = value
    
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
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
        writer.write_collection_of_object_values("customSecurityAttributeDefinitions", self.custom_security_attribute_definitions)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
        writer.write_collection_of_object_values("onPremisesSynchronization", self.on_premises_synchronization)
    

