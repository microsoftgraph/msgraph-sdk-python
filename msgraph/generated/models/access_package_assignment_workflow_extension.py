from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_callout_extension import CustomCalloutExtension
    from .custom_extension_callback_configuration import CustomExtensionCallbackConfiguration

from .custom_callout_extension import CustomCalloutExtension

@dataclass
class AccessPackageAssignmentWorkflowExtension(CustomCalloutExtension):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageAssignmentWorkflowExtension"
    # The callback configuration for a custom extension.
    callback_configuration: Optional[CustomExtensionCallbackConfiguration] = None
    # The userPrincipalName of the user or identity of the subject that created this resource. Read-only.
    created_by: Optional[str] = None
    # When the entity was created.
    created_date_time: Optional[datetime.datetime] = None
    # The userPrincipalName of the identity that last modified the entity.
    last_modified_by: Optional[str] = None
    # When the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentWorkflowExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentWorkflowExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentWorkflowExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_callback_configuration import CustomExtensionCallbackConfiguration

        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_callback_configuration import CustomExtensionCallbackConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackConfiguration": lambda n : setattr(self, 'callback_configuration', n.get_object_value(CustomExtensionCallbackConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("callbackConfiguration", self.callback_configuration)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

