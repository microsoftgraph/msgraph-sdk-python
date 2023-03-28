from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teleconference_device_video_quality

from . import teleconference_device_video_quality

class TeleconferenceDeviceScreenSharingQuality(teleconference_device_video_quality.TeleconferenceDeviceVideoQuality):
    def __init__(self,) -> None:
        """
        Instantiates a new TeleconferenceDeviceScreenSharingQuality and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeleconferenceDeviceScreenSharingQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceScreenSharingQuality
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeleconferenceDeviceScreenSharingQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teleconference_device_video_quality

        fields: Dict[str, Callable[[Any], None]] = {
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
    

