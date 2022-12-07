from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_identifier = lazy_import('msgraph.generated.models.mobile_app_identifier')

class AndroidMobileAppIdentifier(mobile_app_identifier.MobileAppIdentifier):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidMobileAppIdentifier and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidMobileAppIdentifier"
        # The identifier for an app, as specified in the play store.
        self._package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidMobileAppIdentifier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidMobileAppIdentifier
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidMobileAppIdentifier()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. The identifier for an app, as specified in the play store.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. The identifier for an app, as specified in the play store.
        Args:
            value: Value to set for the packageId property.
        """
        self._package_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("packageId", self.package_id)
    

