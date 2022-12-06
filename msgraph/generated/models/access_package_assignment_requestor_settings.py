from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class AccessPackageAssignmentRequestorSettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allow_custom_assignment_schedule(self,) -> Optional[bool]:
        """
        Gets the allowCustomAssignmentSchedule property value. If false, the requestor is not permitted to include a schedule in their request.
        Returns: Optional[bool]
        """
        return self._allow_custom_assignment_schedule
    
    @allow_custom_assignment_schedule.setter
    def allow_custom_assignment_schedule(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowCustomAssignmentSchedule property value. If false, the requestor is not permitted to include a schedule in their request.
        Args:
            value: Value to set for the allowCustomAssignmentSchedule property.
        """
        self._allow_custom_assignment_schedule = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentRequestorSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If false, the requestor is not permitted to include a schedule in their request.
        self._allow_custom_assignment_schedule: Optional[bool] = None
        # If true, allows on-behalf-of requestors to create a request to add access for another principal.
        self._enable_on_behalf_requestors_to_add_access: Optional[bool] = None
        # If true, allows on-behalf-of requestors to create a request to remove access for another principal.
        self._enable_on_behalf_requestors_to_remove_access: Optional[bool] = None
        # If true, allows on-behalf-of requestors to create a request to update access for another principal.
        self._enable_on_behalf_requestors_to_update_access: Optional[bool] = None
        # If true, allows requestors to create a request to add access for themselves.
        self._enable_targets_to_self_add_access: Optional[bool] = None
        # If true, allows requestors to create a request to remove their access.
        self._enable_targets_to_self_remove_access: Optional[bool] = None
        # If true, allows requestors to create a request to update their access.
        self._enable_targets_to_self_update_access: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The principals who can request on-behalf-of others.
        self._on_behalf_requestors: Optional[List[subject_set.SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestorSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequestorSettings()
    
    @property
    def enable_on_behalf_requestors_to_add_access(self,) -> Optional[bool]:
        """
        Gets the enableOnBehalfRequestorsToAddAccess property value. If true, allows on-behalf-of requestors to create a request to add access for another principal.
        Returns: Optional[bool]
        """
        return self._enable_on_behalf_requestors_to_add_access
    
    @enable_on_behalf_requestors_to_add_access.setter
    def enable_on_behalf_requestors_to_add_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableOnBehalfRequestorsToAddAccess property value. If true, allows on-behalf-of requestors to create a request to add access for another principal.
        Args:
            value: Value to set for the enableOnBehalfRequestorsToAddAccess property.
        """
        self._enable_on_behalf_requestors_to_add_access = value
    
    @property
    def enable_on_behalf_requestors_to_remove_access(self,) -> Optional[bool]:
        """
        Gets the enableOnBehalfRequestorsToRemoveAccess property value. If true, allows on-behalf-of requestors to create a request to remove access for another principal.
        Returns: Optional[bool]
        """
        return self._enable_on_behalf_requestors_to_remove_access
    
    @enable_on_behalf_requestors_to_remove_access.setter
    def enable_on_behalf_requestors_to_remove_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableOnBehalfRequestorsToRemoveAccess property value. If true, allows on-behalf-of requestors to create a request to remove access for another principal.
        Args:
            value: Value to set for the enableOnBehalfRequestorsToRemoveAccess property.
        """
        self._enable_on_behalf_requestors_to_remove_access = value
    
    @property
    def enable_on_behalf_requestors_to_update_access(self,) -> Optional[bool]:
        """
        Gets the enableOnBehalfRequestorsToUpdateAccess property value. If true, allows on-behalf-of requestors to create a request to update access for another principal.
        Returns: Optional[bool]
        """
        return self._enable_on_behalf_requestors_to_update_access
    
    @enable_on_behalf_requestors_to_update_access.setter
    def enable_on_behalf_requestors_to_update_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableOnBehalfRequestorsToUpdateAccess property value. If true, allows on-behalf-of requestors to create a request to update access for another principal.
        Args:
            value: Value to set for the enableOnBehalfRequestorsToUpdateAccess property.
        """
        self._enable_on_behalf_requestors_to_update_access = value
    
    @property
    def enable_targets_to_self_add_access(self,) -> Optional[bool]:
        """
        Gets the enableTargetsToSelfAddAccess property value. If true, allows requestors to create a request to add access for themselves.
        Returns: Optional[bool]
        """
        return self._enable_targets_to_self_add_access
    
    @enable_targets_to_self_add_access.setter
    def enable_targets_to_self_add_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableTargetsToSelfAddAccess property value. If true, allows requestors to create a request to add access for themselves.
        Args:
            value: Value to set for the enableTargetsToSelfAddAccess property.
        """
        self._enable_targets_to_self_add_access = value
    
    @property
    def enable_targets_to_self_remove_access(self,) -> Optional[bool]:
        """
        Gets the enableTargetsToSelfRemoveAccess property value. If true, allows requestors to create a request to remove their access.
        Returns: Optional[bool]
        """
        return self._enable_targets_to_self_remove_access
    
    @enable_targets_to_self_remove_access.setter
    def enable_targets_to_self_remove_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableTargetsToSelfRemoveAccess property value. If true, allows requestors to create a request to remove their access.
        Args:
            value: Value to set for the enableTargetsToSelfRemoveAccess property.
        """
        self._enable_targets_to_self_remove_access = value
    
    @property
    def enable_targets_to_self_update_access(self,) -> Optional[bool]:
        """
        Gets the enableTargetsToSelfUpdateAccess property value. If true, allows requestors to create a request to update their access.
        Returns: Optional[bool]
        """
        return self._enable_targets_to_self_update_access
    
    @enable_targets_to_self_update_access.setter
    def enable_targets_to_self_update_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableTargetsToSelfUpdateAccess property value. If true, allows requestors to create a request to update their access.
        Args:
            value: Value to set for the enableTargetsToSelfUpdateAccess property.
        """
        self._enable_targets_to_self_update_access = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_custom_assignment_schedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "enable_on_behalf_requestors_to_add_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_add_access', n.get_bool_value()),
            "enable_on_behalf_requestors_to_remove_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_remove_access', n.get_bool_value()),
            "enable_on_behalf_requestors_to_update_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_update_access', n.get_bool_value()),
            "enable_targets_to_self_add_access": lambda n : setattr(self, 'enable_targets_to_self_add_access', n.get_bool_value()),
            "enable_targets_to_self_remove_access": lambda n : setattr(self, 'enable_targets_to_self_remove_access', n.get_bool_value()),
            "enable_targets_to_self_update_access": lambda n : setattr(self, 'enable_targets_to_self_update_access', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_behalf_requestors": lambda n : setattr(self, 'on_behalf_requestors', n.get_collection_of_object_values(subject_set.SubjectSet)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def on_behalf_requestors(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the onBehalfRequestors property value. The principals who can request on-behalf-of others.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._on_behalf_requestors
    
    @on_behalf_requestors.setter
    def on_behalf_requestors(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the onBehalfRequestors property value. The principals who can request on-behalf-of others.
        Args:
            value: Value to set for the onBehalfRequestors property.
        """
        self._on_behalf_requestors = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowCustomAssignmentSchedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("enableOnBehalfRequestorsToAddAccess", self.enable_on_behalf_requestors_to_add_access)
        writer.write_bool_value("enableOnBehalfRequestorsToRemoveAccess", self.enable_on_behalf_requestors_to_remove_access)
        writer.write_bool_value("enableOnBehalfRequestorsToUpdateAccess", self.enable_on_behalf_requestors_to_update_access)
        writer.write_bool_value("enableTargetsToSelfAddAccess", self.enable_targets_to_self_add_access)
        writer.write_bool_value("enableTargetsToSelfRemoveAccess", self.enable_targets_to_self_remove_access)
        writer.write_bool_value("enableTargetsToSelfUpdateAccess", self.enable_targets_to_self_update_access)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onBehalfRequestors", self.on_behalf_requestors)
        writer.write_additional_data_value(self.additional_data)
    

