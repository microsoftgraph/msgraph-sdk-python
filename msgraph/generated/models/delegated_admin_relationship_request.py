from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_relationship_request_action, delegated_admin_relationship_request_status, entity

from . import entity

@dataclass
class DelegatedAdminRelationshipRequest(entity.Entity):
    # The action property
    action: Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction] = None
    # The date and time in ISO 8601 format and in UTC time when the relationship request was created. Read-only.
    created_date_time: Optional[datetime] = None
    # The date and time in ISO 8601 format and UTC time when this relationship request was last modified. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the request. Read-only. The possible values are: created, pending, succeeded, failed, unknownFutureValue.
    status: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminRelationshipRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationshipRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminRelationshipRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_relationship_request_action, delegated_admin_relationship_request_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus)),
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
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

