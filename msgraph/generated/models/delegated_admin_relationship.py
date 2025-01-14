from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
    from .delegated_admin_access_details import DelegatedAdminAccessDetails
    from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
    from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
    from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
    from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
    from .entity import Entity
    from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

from .entity import Entity

@dataclass
class DelegatedAdminRelationship(Entity, Parsable):
    # The access assignments associated with the delegated admin relationship.
    access_assignments: Optional[list[DelegatedAdminAccessAssignment]] = None
    # The accessDetails property
    access_details: Optional[DelegatedAdminAccessDetails] = None
    # The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only.
    activated_date_time: Optional[datetime.datetime] = None
    # The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended.
    auto_extend_duration: Optional[datetime.timedelta] = None
    # The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Can't be changed by the customer.
    customer: Optional[DelegatedAdminRelationshipCustomerParticipant] = None
    # The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner and is set by the partner only when the relationship is in the created status and can't be changed by the customer. Maximum length is 50 characters.
    display_name: Optional[str] = None
    # The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer.
    duration: Optional[datetime.timedelta] = None
    # The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The long running operations associated with the delegated admin relationship.
    operations: Optional[list[DelegatedAdminRelationshipOperation]] = None
    # The requests associated with the delegated admin relationship.
    requests: Optional[list[DelegatedAdminRelationshipRequest]] = None
    # The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderby.
    status: Optional[DelegatedAdminRelationshipStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationship
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resellerDelegatedAdminRelationship".casefold():
            from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

            return ResellerDelegatedAdminRelationship()
        return DelegatedAdminRelationship()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_access_details import DelegatedAdminAccessDetails
        from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
        from .entity import Entity
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_access_details import DelegatedAdminAccessDetails
        from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
        from .entity import Entity
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

        fields: dict[str, Callable[[Any], None]] = {
            "accessAssignments": lambda n : setattr(self, 'access_assignments', n.get_collection_of_object_values(DelegatedAdminAccessAssignment)),
            "accessDetails": lambda n : setattr(self, 'access_details', n.get_object_value(DelegatedAdminAccessDetails)),
            "activatedDateTime": lambda n : setattr(self, 'activated_date_time', n.get_datetime_value()),
            "autoExtendDuration": lambda n : setattr(self, 'auto_extend_duration', n.get_timedelta_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(DelegatedAdminRelationshipCustomerParticipant)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(DelegatedAdminRelationshipOperation)),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(DelegatedAdminRelationshipRequest)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DelegatedAdminRelationshipStatus)),
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
        writer.write_collection_of_object_values("accessAssignments", self.access_assignments)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("activatedDateTime", self.activated_date_time)
        writer.write_timedelta_value("autoExtendDuration", self.auto_extend_duration)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customer", self.customer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_enum_value("status", self.status)
    

