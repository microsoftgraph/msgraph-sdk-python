from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .entity import Entity
    from .install_intent import InstallIntent
    from .ios_vpp_e_book_assignment import IosVppEBookAssignment

from .entity import Entity

@dataclass
class ManagedEBookAssignment(Entity, Parsable):
    """
    Contains properties used to assign a eBook to a group.
    """
    # Possible values for the install intent chosen by the admin.
    install_intent: Optional[InstallIntent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The assignment target for eBook.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedEBookAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedEBookAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBookAssignment".casefold():
            from .ios_vpp_e_book_assignment import IosVppEBookAssignment

            return IosVppEBookAssignment()
        return ManagedEBookAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity
        from .install_intent import InstallIntent
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity
        from .install_intent import InstallIntent
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "installIntent": lambda n : setattr(self, 'install_intent', n.get_enum_value(InstallIntent)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_enum_value("installIntent", self.install_intent)
        writer.write_object_value("target", self.target)
    

