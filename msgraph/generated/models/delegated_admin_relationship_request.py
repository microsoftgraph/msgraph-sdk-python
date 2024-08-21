from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
    from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class DelegatedAdminRelationshipRequest(Entity):
    # The action property
    action: Optional[DelegatedAdminRelationshipRequestAction] = None
    # The date and time in ISO 8601 format and in UTC time when the relationship request was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time in ISO 8601 format and UTC time when this relationship request was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the request. Read-only. The possible values are: created, pending, succeeded, failed, unknownFutureValue.
    status: Optional[DelegatedAdminRelationshipRequestStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminRelationshipRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationshipRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminRelationshipRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
        from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus
        from .entity import Entity

        from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
        from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(DelegatedAdminRelationshipRequestAction)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DelegatedAdminRelationshipRequestStatus)),
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
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

