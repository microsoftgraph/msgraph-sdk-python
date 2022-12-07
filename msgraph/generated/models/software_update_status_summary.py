from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class SoftwareUpdateStatusSummary(entity.Entity):
    @property
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. Number of compliant devices.
        Returns: Optional[int]
        """
        return self._compliant_device_count
    
    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. Number of compliant devices.
        Args:
            value: Value to set for the compliantDeviceCount property.
        """
        self._compliant_device_count = value
    
    @property
    def compliant_user_count(self,) -> Optional[int]:
        """
        Gets the compliantUserCount property value. Number of compliant users.
        Returns: Optional[int]
        """
        return self._compliant_user_count
    
    @compliant_user_count.setter
    def compliant_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantUserCount property value. Number of compliant users.
        Args:
            value: Value to set for the compliantUserCount property.
        """
        self._compliant_user_count = value
    
    @property
    def conflict_device_count(self,) -> Optional[int]:
        """
        Gets the conflictDeviceCount property value. Number of conflict devices.
        Returns: Optional[int]
        """
        return self._conflict_device_count
    
    @conflict_device_count.setter
    def conflict_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictDeviceCount property value. Number of conflict devices.
        Args:
            value: Value to set for the conflictDeviceCount property.
        """
        self._conflict_device_count = value
    
    @property
    def conflict_user_count(self,) -> Optional[int]:
        """
        Gets the conflictUserCount property value. Number of conflict users.
        Returns: Optional[int]
        """
        return self._conflict_user_count
    
    @conflict_user_count.setter
    def conflict_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictUserCount property value. Number of conflict users.
        Args:
            value: Value to set for the conflictUserCount property.
        """
        self._conflict_user_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new softwareUpdateStatusSummary and sets the default values.
        """
        super().__init__()
        # Number of compliant devices.
        self._compliant_device_count: Optional[int] = None
        # Number of compliant users.
        self._compliant_user_count: Optional[int] = None
        # Number of conflict devices.
        self._conflict_device_count: Optional[int] = None
        # Number of conflict users.
        self._conflict_user_count: Optional[int] = None
        # The name of the policy.
        self._display_name: Optional[str] = None
        # Number of devices had error.
        self._error_device_count: Optional[int] = None
        # Number of users had error.
        self._error_user_count: Optional[int] = None
        # Number of non compliant devices.
        self._non_compliant_device_count: Optional[int] = None
        # Number of non compliant users.
        self._non_compliant_user_count: Optional[int] = None
        # Number of not applicable devices.
        self._not_applicable_device_count: Optional[int] = None
        # Number of not applicable users.
        self._not_applicable_user_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of remediated devices.
        self._remediated_device_count: Optional[int] = None
        # Number of remediated users.
        self._remediated_user_count: Optional[int] = None
        # Number of unknown devices.
        self._unknown_device_count: Optional[int] = None
        # Number of unknown users.
        self._unknown_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareUpdateStatusSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateStatusSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SoftwareUpdateStatusSummary()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Number of devices had error.
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Number of devices had error.
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value
    
    @property
    def error_user_count(self,) -> Optional[int]:
        """
        Gets the errorUserCount property value. Number of users had error.
        Returns: Optional[int]
        """
        return self._error_user_count
    
    @error_user_count.setter
    def error_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorUserCount property value. Number of users had error.
        Args:
            value: Value to set for the errorUserCount property.
        """
        self._error_user_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "compliant_user_count": lambda n : setattr(self, 'compliant_user_count', n.get_int_value()),
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "conflict_user_count": lambda n : setattr(self, 'conflict_user_count', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "error_user_count": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "non_compliant_user_count": lambda n : setattr(self, 'non_compliant_user_count', n.get_int_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "not_applicable_user_count": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "remediated_user_count": lambda n : setattr(self, 'remediated_user_count', n.get_int_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
            "unknown_user_count": lambda n : setattr(self, 'unknown_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def non_compliant_device_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantDeviceCount property value. Number of non compliant devices.
        Returns: Optional[int]
        """
        return self._non_compliant_device_count
    
    @non_compliant_device_count.setter
    def non_compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantDeviceCount property value. Number of non compliant devices.
        Args:
            value: Value to set for the nonCompliantDeviceCount property.
        """
        self._non_compliant_device_count = value
    
    @property
    def non_compliant_user_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantUserCount property value. Number of non compliant users.
        Returns: Optional[int]
        """
        return self._non_compliant_user_count
    
    @non_compliant_user_count.setter
    def non_compliant_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantUserCount property value. Number of non compliant users.
        Args:
            value: Value to set for the nonCompliantUserCount property.
        """
        self._non_compliant_user_count = value
    
    @property
    def not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the notApplicableDeviceCount property value. Number of not applicable devices.
        Returns: Optional[int]
        """
        return self._not_applicable_device_count
    
    @not_applicable_device_count.setter
    def not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableDeviceCount property value. Number of not applicable devices.
        Args:
            value: Value to set for the notApplicableDeviceCount property.
        """
        self._not_applicable_device_count = value
    
    @property
    def not_applicable_user_count(self,) -> Optional[int]:
        """
        Gets the notApplicableUserCount property value. Number of not applicable users.
        Returns: Optional[int]
        """
        return self._not_applicable_user_count
    
    @not_applicable_user_count.setter
    def not_applicable_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableUserCount property value. Number of not applicable users.
        Args:
            value: Value to set for the notApplicableUserCount property.
        """
        self._not_applicable_user_count = value
    
    @property
    def remediated_device_count(self,) -> Optional[int]:
        """
        Gets the remediatedDeviceCount property value. Number of remediated devices.
        Returns: Optional[int]
        """
        return self._remediated_device_count
    
    @remediated_device_count.setter
    def remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedDeviceCount property value. Number of remediated devices.
        Args:
            value: Value to set for the remediatedDeviceCount property.
        """
        self._remediated_device_count = value
    
    @property
    def remediated_user_count(self,) -> Optional[int]:
        """
        Gets the remediatedUserCount property value. Number of remediated users.
        Returns: Optional[int]
        """
        return self._remediated_user_count
    
    @remediated_user_count.setter
    def remediated_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedUserCount property value. Number of remediated users.
        Args:
            value: Value to set for the remediatedUserCount property.
        """
        self._remediated_user_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("compliantUserCount", self.compliant_user_count)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("conflictUserCount", self.conflict_user_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_int_value("nonCompliantUserCount", self.non_compliant_user_count)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("notApplicableUserCount", self.not_applicable_user_count)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_int_value("remediatedUserCount", self.remediated_user_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
        writer.write_int_value("unknownUserCount", self.unknown_user_count)
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Number of unknown devices.
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Number of unknown devices.
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value
    
    @property
    def unknown_user_count(self,) -> Optional[int]:
        """
        Gets the unknownUserCount property value. Number of unknown users.
        Returns: Optional[int]
        """
        return self._unknown_user_count
    
    @unknown_user_count.setter
    def unknown_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownUserCount property value. Number of unknown users.
        Args:
            value: Value to set for the unknownUserCount property.
        """
        self._unknown_user_count = value
    

