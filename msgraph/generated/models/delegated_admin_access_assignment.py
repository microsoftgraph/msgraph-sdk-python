from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_admin_access_assignment_status = lazy_import('msgraph.generated.models.delegated_admin_access_assignment_status')
delegated_admin_access_container = lazy_import('msgraph.generated.models.delegated_admin_access_container')
delegated_admin_access_details = lazy_import('msgraph.generated.models.delegated_admin_access_details')
entity = lazy_import('msgraph.generated.models.entity')

class DelegatedAdminAccessAssignment(entity.Entity):
    @property
    def access_container(self,) -> Optional[delegated_admin_access_container.DelegatedAdminAccessContainer]:
        """
        Gets the accessContainer property value. 
        Returns: Optional[delegated_admin_access_container.DelegatedAdminAccessContainer]
        """
        return self._access_container
    
    @access_container.setter
    def access_container(self,value: Optional[delegated_admin_access_container.DelegatedAdminAccessContainer] = None) -> None:
        """
        Sets the accessContainer property value. 
        Args:
            value: Value to set for the accessContainer property.
        """
        self._access_container = value
    
    @property
    def access_details(self,) -> Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]:
        """
        Gets the accessDetails property value. 
        Returns: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]
        """
        return self._access_details
    
    @access_details.setter
    def access_details(self,value: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None) -> None:
        """
        Sets the accessDetails property value. 
        Args:
            value: Value to set for the accessDetails property.
        """
        self._access_details = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DelegatedAdminAccessAssignment and sets the default values.
        """
        super().__init__()
        self._access_container: Optional[delegated_admin_access_container.DelegatedAdminAccessContainer] = None
        self._access_details: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None
        self._created_date_time: Optional[datetime] = None
        self._last_modified_date_time: Optional[datetime] = None
        self.odata_type: Optional[str] = None
        self._status: Optional[delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. 
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. 
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminAccessAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminAccessAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminAccessAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accessContainer": lambda n : setattr(self, 'access_container', n.get_object_value(delegated_admin_access_container.DelegatedAdminAccessContainer)),
            "accessDetails": lambda n : setattr(self, 'access_details', n.get_object_value(delegated_admin_access_details.DelegatedAdminAccessDetails)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. 
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. 
        Args:
            value: Value to set for the lastModifiedDateTime property.
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
        writer.write_object_value("accessContainer", self.access_container)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus]:
        """
        Gets the status property value. 
        Returns: Optional[delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus] = None) -> None:
        """
        Sets the status property value. 
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

