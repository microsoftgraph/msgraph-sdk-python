from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_identifier = lazy_import('msgraph.generated.models.mobile_app_identifier')

class IosMobileAppIdentifier(mobile_app_identifier.MobileAppIdentifier):
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The identifier for an app, as specified in the app store.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The identifier for an app, as specified in the app store.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosMobileAppIdentifier and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosMobileAppIdentifier"
        # The identifier for an app, as specified in the app store.
        self._bundle_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosMobileAppIdentifier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosMobileAppIdentifier
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosMobileAppIdentifier()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("bundleId", self.bundle_id)
    

