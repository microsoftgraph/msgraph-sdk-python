from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_target = lazy_import('msgraph.generated.models.device_and_app_management_assignment_target')
entity = lazy_import('msgraph.generated.models.entity')
install_intent = lazy_import('msgraph.generated.models.install_intent')

class ManagedEBookAssignment(entity.Entity):
    """
    Contains properties used to assign a eBook to a group.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedEBookAssignment and sets the default values.
        """
        super().__init__()
        # Possible values for the install intent chosen by the admin.
        self._install_intent: Optional[install_intent.InstallIntent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The assignment target for eBook.
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedEBookAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedEBookAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedEBookAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "install_intent": lambda n : setattr(self, 'install_intent', n.get_enum_value(install_intent.InstallIntent)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_intent(self,) -> Optional[install_intent.InstallIntent]:
        """
        Gets the installIntent property value. Possible values for the install intent chosen by the admin.
        Returns: Optional[install_intent.InstallIntent]
        """
        return self._install_intent
    
    @install_intent.setter
    def install_intent(self,value: Optional[install_intent.InstallIntent] = None) -> None:
        """
        Sets the installIntent property value. Possible values for the install intent chosen by the admin.
        Args:
            value: Value to set for the installIntent property.
        """
        self._install_intent = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("installIntent", self.install_intent)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. The assignment target for eBook.
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The assignment target for eBook.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

