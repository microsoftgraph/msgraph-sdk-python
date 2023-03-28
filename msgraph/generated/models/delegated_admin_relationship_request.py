from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_relationship_request_action, delegated_admin_relationship_request_status, entity

from . import entity

class DelegatedAdminRelationshipRequest(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedAdminRelationshipRequest and sets the default values.
        """
        super().__init__()
        # The action property
        self._action: Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction] = None
        # The date and time in ISO 8601 format and in UTC time when the relationship request was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The date and time in ISO 8601 format and UTC time when this relationship request was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of the request. Read-only. The possible values are: created, pending, succeeded, failed, unknownFutureValue.
        self._status: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus] = None
    
    @property
    def action(self,) -> Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction]:
        """
        Gets the action property value. The action property
        Returns: Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction] = None) -> None:
        """
        Sets the action property value. The action property
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship request was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship request was created. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
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
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time in ISO 8601 format and UTC time when this relationship request was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time in ISO 8601 format and UTC time when this relationship request was last modified. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
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
    
    @property
    def status(self,) -> Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus]:
        """
        Gets the status property value. The status of the request. Read-only. The possible values are: created, pending, succeeded, failed, unknownFutureValue.
        Returns: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus] = None) -> None:
        """
        Sets the status property value. The status of the request. Read-only. The possible values are: created, pending, succeeded, failed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

