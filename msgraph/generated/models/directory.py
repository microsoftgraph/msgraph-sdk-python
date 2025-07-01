from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .administrative_unit import AdministrativeUnit
    from .attribute_set import AttributeSet
    from .company_subscription import CompanySubscription
    from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
    from .device_local_credential_info import DeviceLocalCredentialInfo
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .identity_provider_base import IdentityProviderBase
    from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
    from .public_key_infrastructure_root import PublicKeyInfrastructureRoot

from .entity import Entity

@dataclass
class Directory(Entity, Parsable):
    # Conceptual container for user and group directory objects.
    administrative_units: Optional[list[AdministrativeUnit]] = None
    # Group of related custom security attribute definitions.
    attribute_sets: Optional[list[AttributeSet]] = None
    # Schema of a custom security attributes (key-value pairs).
    custom_security_attribute_definitions: Optional[list[CustomSecurityAttributeDefinition]] = None
    # Recently deleted items. Read-only. Nullable.
    deleted_items: Optional[list[DirectoryObject]] = None
    # The credentials of the device's local administrator account backed up to Microsoft Entra ID.
    device_local_credentials: Optional[list[DeviceLocalCredentialInfo]] = None
    # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
    federation_configurations: Optional[list[IdentityProviderBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A container for on-premises directory synchronization functionalities that are available for the organization.
    on_premises_synchronization: Optional[list[OnPremisesDirectorySynchronization]] = None
    # The collection of public key infrastructure instances for the certificate-based authentication feature for users in a Microsoft Entra tenant.
    public_key_infrastructure: Optional[PublicKeyInfrastructureRoot] = None
    # List of commercial subscriptions that an organization acquired.
    subscriptions: Optional[list[CompanySubscription]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Directory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .administrative_unit import AdministrativeUnit
        from .attribute_set import AttributeSet
        from .company_subscription import CompanySubscription
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .identity_provider_base import IdentityProviderBase
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .public_key_infrastructure_root import PublicKeyInfrastructureRoot

        from .administrative_unit import AdministrativeUnit
        from .attribute_set import AttributeSet
        from .company_subscription import CompanySubscription
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .identity_provider_base import IdentityProviderBase
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .public_key_infrastructure_root import PublicKeyInfrastructureRoot

        fields: dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(AdministrativeUnit)),
            "attributeSets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(AttributeSet)),
            "customSecurityAttributeDefinitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(CustomSecurityAttributeDefinition)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(DirectoryObject)),
            "deviceLocalCredentials": lambda n : setattr(self, 'device_local_credentials', n.get_collection_of_object_values(DeviceLocalCredentialInfo)),
            "federationConfigurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(IdentityProviderBase)),
            "onPremisesSynchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(OnPremisesDirectorySynchronization)),
            "publicKeyInfrastructure": lambda n : setattr(self, 'public_key_infrastructure', n.get_object_value(PublicKeyInfrastructureRoot)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(CompanySubscription)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
        writer.write_collection_of_object_values("customSecurityAttributeDefinitions", self.custom_security_attribute_definitions)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("deviceLocalCredentials", self.device_local_credentials)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
        writer.write_collection_of_object_values("onPremisesSynchronization", self.on_premises_synchronization)
        writer.write_object_value("publicKeyInfrastructure", self.public_key_infrastructure)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
    

