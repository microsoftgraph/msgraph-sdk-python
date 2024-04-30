from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
    from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

@dataclass
class MultiTenantOrganizationMemberTransitionDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Role of the tenant in the multitenant organization. The possible values are: owner, member, unknownFutureValue.
    desired_role: Optional[MultiTenantOrganizationMemberRole] = None
    # State of the tenant in the multitenant organization currently being processed. The possible values are: pending, active, removed, unknownFutureValue. Read-only.
    desired_state: Optional[MultiTenantOrganizationMemberState] = None
    # Details that explain the processing status if any. Read-only.
    details: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Processing state of the asynchronous job. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue. Read-only.
    status: Optional[MultiTenantOrganizationMemberProcessingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MultiTenantOrganizationMemberTransitionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationMemberTransitionDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationMemberTransitionDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        fields: Dict[str, Callable[[Any], None]] = {
            "desiredRole": lambda n : setattr(self, 'desired_role', n.get_enum_value(MultiTenantOrganizationMemberRole)),
            "desiredState": lambda n : setattr(self, 'desired_state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MultiTenantOrganizationMemberProcessingStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("desiredRole", self.desired_role)
        writer.write_enum_value("desiredState", self.desired_state)
        writer.write_str_value("details", self.details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

