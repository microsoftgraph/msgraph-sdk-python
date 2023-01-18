from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_contained_app = lazy_import('msgraph.generated.models.mobile_contained_app')

class WindowsUniversalAppXContainedApp(mobile_contained_app.MobileContainedApp):
    @property
    def app_user_model_id(self,) -> Optional[str]:
        """
        Gets the appUserModelId property value. The app user model ID of the contained app of a WindowsUniversalAppX app.
        Returns: Optional[str]
        """
        return self._app_user_model_id
    
    @app_user_model_id.setter
    def app_user_model_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appUserModelId property value. The app user model ID of the contained app of a WindowsUniversalAppX app.
        Args:
            value: Value to set for the appUserModelId property.
        """
        self._app_user_model_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsUniversalAppXContainedApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUniversalAppXContainedApp"
        # The app user model ID of the contained app of a WindowsUniversalAppX app.
        self._app_user_model_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUniversalAppXContainedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUniversalAppXContainedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUniversalAppXContainedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_user_model_id": lambda n : setattr(self, 'app_user_model_id', n.get_str_value()),
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
        writer.write_str_value("appUserModelId", self.app_user_model_id)
    

