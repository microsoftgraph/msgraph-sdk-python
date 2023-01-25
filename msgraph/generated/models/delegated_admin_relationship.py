from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_admin_access_assignment = lazy_import('msgraph.generated.models.delegated_admin_access_assignment')
delegated_admin_access_details = lazy_import('msgraph.generated.models.delegated_admin_access_details')
delegated_admin_relationship_customer_participant = lazy_import('msgraph.generated.models.delegated_admin_relationship_customer_participant')
delegated_admin_relationship_operation = lazy_import('msgraph.generated.models.delegated_admin_relationship_operation')
delegated_admin_relationship_request = lazy_import('msgraph.generated.models.delegated_admin_relationship_request')
delegated_admin_relationship_status = lazy_import('msgraph.generated.models.delegated_admin_relationship_status')
entity = lazy_import('msgraph.generated.models.entity')

class DelegatedAdminRelationship(entity.Entity):
    @property
    def access_assignments(self,) -> Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]]:
        """
        Gets the accessAssignments property value. The accessAssignments property
        Returns: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]]
        """
        return self._access_assignments
    
    @access_assignments.setter
    def access_assignments(self,value: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]] = None) -> None:
        """
        Sets the accessAssignments property value. The accessAssignments property
        Args:
            value: Value to set for the accessAssignments property.
        """
        self._access_assignments = value
    
    @property
    def access_details(self,) -> Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]:
        """
        Gets the accessDetails property value. The accessDetails property
        Returns: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]
        """
        return self._access_details
    
    @access_details.setter
    def access_details(self,value: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None) -> None:
        """
        Sets the accessDetails property value. The accessDetails property
        Args:
            value: Value to set for the accessDetails property.
        """
        self._access_details = value
    
    @property
    def activated_date_time(self,) -> Optional[datetime]:
        """
        Gets the activatedDateTime property value. The activatedDateTime property
        Returns: Optional[datetime]
        """
        return self._activated_date_time
    
    @activated_date_time.setter
    def activated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activatedDateTime property value. The activatedDateTime property
        Args:
            value: Value to set for the activatedDateTime property.
        """
        self._activated_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DelegatedAdminRelationship and sets the default values.
        """
        super().__init__()
        # The accessAssignments property
        self._access_assignments: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]] = None
        # The accessDetails property
        self._access_details: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None
        # The activatedDateTime property
        self._activated_date_time: Optional[datetime] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The customer property
        self._customer: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The duration property
        self._duration: Optional[Timedelta] = None
        # The endDateTime property
        self._end_date_time: Optional[datetime] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]] = None
        # The requests property
        self._requests: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]] = None
        # The status property
        self._status: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus] = None
    
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
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationship
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminRelationship()
    
    @property
    def customer(self,) -> Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant]:
        """
        Gets the customer property value. The customer property
        Returns: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant]
        """
        return self._customer
    
    @customer.setter
    def customer(self,value: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant] = None) -> None:
        """
        Sets the customer property value. The customer property
        Args:
            value: Value to set for the customer property.
        """
        self._customer = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def duration(self,) -> Optional[Timedelta]:
        """
        Gets the duration property value. The duration property
        Returns: Optional[Timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the duration property value. The duration property
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_assignments": lambda n : setattr(self, 'access_assignments', n.get_collection_of_object_values(delegated_admin_access_assignment.DelegatedAdminAccessAssignment)),
            "access_details": lambda n : setattr(self, 'access_details', n.get_object_value(delegated_admin_access_details.DelegatedAdminAccessDetails)),
            "activated_date_time": lambda n : setattr(self, 'activated_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_object_value(Timedelta)),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation)),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(delegated_admin_relationship_request.DelegatedAdminRelationshipRequest)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(delegated_admin_relationship_status.DelegatedAdminRelationshipStatus)),
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
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def operations(self,) -> Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def requests(self,) -> Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]]:
        """
        Gets the requests property value. The requests property
        Returns: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]]
        """
        return self._requests
    
    @requests.setter
    def requests(self,value: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]] = None) -> None:
        """
        Sets the requests property value. The requests property
        Args:
            value: Value to set for the requests property.
        """
        self._requests = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessAssignments", self.access_assignments)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("activatedDateTime", self.activated_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customer", self.customer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

