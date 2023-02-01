from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_admin_relationship_request_action = lazy_import('msgraph.generated.models.delegated_admin_relationship_request_action')
delegated_admin_relationship_request_status = lazy_import('msgraph.generated.models.delegated_admin_relationship_request_status')
entity = lazy_import('msgraph.generated.models.entity')

class DelegatedAdminRelationshipRequest(entity.Entity):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedAdminRelationshipRequest and sets the default values.
        """
        super().__init__()
        # The action property
        self._action: Optional[delegated_admin_relationship_request_action.DelegatedAdminRelationshipRequestAction] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
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
        fields = {
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
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
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
        Gets the status property value. The status property
        Returns: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[delegated_admin_relationship_request_status.DelegatedAdminRelationshipRequestStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

