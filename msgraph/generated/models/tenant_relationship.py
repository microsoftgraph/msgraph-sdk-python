from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_customer import DelegatedAdminCustomer
    from .delegated_admin_relationship import DelegatedAdminRelationship
    from .multi_tenant_organization import MultiTenantOrganization

@dataclass
class TenantRelationship(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The customer who has a delegated admin relationship with a Microsoft partner.
    delegated_admin_customers: Optional[list[DelegatedAdminCustomer]] = None
    # The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
    delegated_admin_relationships: Optional[list[DelegatedAdminRelationship]] = None
    # Defines an organization with more than one instance of Microsoft Entra ID.
    multi_tenant_organization: Optional[MultiTenantOrganization] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantRelationship
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantRelationship()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .multi_tenant_organization import MultiTenantOrganization

        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .multi_tenant_organization import MultiTenantOrganization

        fields: dict[str, Callable[[Any], None]] = {
            "delegatedAdminCustomers": lambda n : setattr(self, 'delegated_admin_customers', n.get_collection_of_object_values(DelegatedAdminCustomer)),
            "delegatedAdminRelationships": lambda n : setattr(self, 'delegated_admin_relationships', n.get_collection_of_object_values(DelegatedAdminRelationship)),
            "multiTenantOrganization": lambda n : setattr(self, 'multi_tenant_organization', n.get_object_value(MultiTenantOrganization)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("delegatedAdminCustomers", self.delegated_admin_customers)
        writer.write_collection_of_object_values("delegatedAdminRelationships", self.delegated_admin_relationships)
        writer.write_object_value("multiTenantOrganization", self.multi_tenant_organization)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

