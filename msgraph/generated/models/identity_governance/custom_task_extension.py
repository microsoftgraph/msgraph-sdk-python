from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..custom_callout_extension import CustomCalloutExtension
    from ..custom_extension_callback_configuration import CustomExtensionCallbackConfiguration
    from ..user import User

from ..custom_callout_extension import CustomCalloutExtension

@dataclass
class CustomTaskExtension(CustomCalloutExtension, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.customTaskExtension"
    # The callback configuration for a custom task extension.
    callback_configuration: Optional[CustomExtensionCallbackConfiguration] = None
    # The unique identifier of the Microsoft Entra user that created the custom task extension.Supports $filter(eq, ne) and $expand.
    created_by: Optional[User] = None
    # When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the Microsoft Entra user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
    last_modified_by: Optional[User] = None
    # When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    last_modified_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomTaskExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..custom_callout_extension import CustomCalloutExtension
        from ..custom_extension_callback_configuration import CustomExtensionCallbackConfiguration
        from ..user import User

        from ..custom_callout_extension import CustomCalloutExtension
        from ..custom_extension_callback_configuration import CustomExtensionCallbackConfiguration
        from ..user import User

        fields: dict[str, Callable[[Any], None]] = {
            "callbackConfiguration": lambda n : setattr(self, 'callback_configuration', n.get_object_value(CustomExtensionCallbackConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(User)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

