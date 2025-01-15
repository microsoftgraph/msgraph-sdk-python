from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_identifier import MobileAppIdentifier

from .entity import Entity

@dataclass
class ManagedMobileApp(Entity, Parsable):
    """
    The identifier for the deployment an app.
    """
    # The identifier for an app with it's operating system type.
    mobile_app_identifier: Optional[MobileAppIdentifier] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedMobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedMobileApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedMobileApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_identifier import MobileAppIdentifier

        from .entity import Entity
        from .mobile_app_identifier import MobileAppIdentifier

        fields: dict[str, Callable[[Any], None]] = {
            "mobileAppIdentifier": lambda n : setattr(self, 'mobile_app_identifier', n.get_object_value(MobileAppIdentifier)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("mobileAppIdentifier", self.mobile_app_identifier)
        writer.write_str_value("version", self.version)
    

