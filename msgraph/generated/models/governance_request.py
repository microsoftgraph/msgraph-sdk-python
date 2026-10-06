from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .relationship_policy import RelationshipPolicy
    from .request_status import RequestStatus
    from .tenant_governance_policy_template import TenantGovernancePolicyTemplate

from .entity import Entity

@dataclass
class GovernanceRequest(Entity, Parsable):
    # The date and time when the request expires if not accepted or rejected. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. Supports $filter (lt, le, gt, ge, eq, ne) and $orderBy.
    expiration_date_time: Optional[datetime.datetime] = None
    # The governance policy template associated with this request.
    governance_policy_template: Optional[TenantGovernancePolicyTemplate] = None
    # The Microsoft Entra tenant ID of the governed tenant. Supports $filter (eq, ne) and $orderBy.
    governed_tenant_id: Optional[str] = None
    # The display name of the governed tenant. Supports $filter (eq, ne) and $orderBy.
    governed_tenant_name: Optional[str] = None
    # The Microsoft Entra tenant ID of the governing tenant. Supports $filter (eq, ne) and $orderBy.
    governing_tenant_id: Optional[str] = None
    # The display name of the governing tenant. Supports $filter (eq, ne) and $orderBy.
    governing_tenant_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policySnapshot property
    policy_snapshot: Optional[RelationshipPolicy] = None
    # The date and time when the request was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. Supports $filter (lt, le, gt, ge, eq, ne) and $orderBy.
    request_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[RequestStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .relationship_policy import RelationshipPolicy
        from .request_status import RequestStatus
        from .tenant_governance_policy_template import TenantGovernancePolicyTemplate

        from .entity import Entity
        from .relationship_policy import RelationshipPolicy
        from .request_status import RequestStatus
        from .tenant_governance_policy_template import TenantGovernancePolicyTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "governancePolicyTemplate": lambda n : setattr(self, 'governance_policy_template', n.get_object_value(TenantGovernancePolicyTemplate)),
            "governedTenantId": lambda n : setattr(self, 'governed_tenant_id', n.get_str_value()),
            "governedTenantName": lambda n : setattr(self, 'governed_tenant_name', n.get_str_value()),
            "governingTenantId": lambda n : setattr(self, 'governing_tenant_id', n.get_str_value()),
            "governingTenantName": lambda n : setattr(self, 'governing_tenant_name', n.get_str_value()),
            "policySnapshot": lambda n : setattr(self, 'policy_snapshot', n.get_object_value(RelationshipPolicy)),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RequestStatus)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("governancePolicyTemplate", self.governance_policy_template)
        writer.write_str_value("governedTenantId", self.governed_tenant_id)
        writer.write_str_value("governedTenantName", self.governed_tenant_name)
        writer.write_str_value("governingTenantId", self.governing_tenant_id)
        writer.write_str_value("governingTenantName", self.governing_tenant_name)
        writer.write_object_value("policySnapshot", self.policy_snapshot)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_enum_value("status", self.status)
    

