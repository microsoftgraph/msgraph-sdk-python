from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .oma_setting_base64 import OmaSettingBase64
    from .oma_setting_boolean import OmaSettingBoolean
    from .oma_setting_date_time import OmaSettingDateTime
    from .oma_setting_floating_point import OmaSettingFloatingPoint
    from .oma_setting_integer import OmaSettingInteger
    from .oma_setting_string import OmaSettingString
    from .oma_setting_string_xml import OmaSettingStringXml

@dataclass
class OmaSetting(AdditionalDataHolder, BackedModel, Parsable):
    """
    OMA Settings definition.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Description.
    description: Optional[str] = None
    # Display Name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OMA.
    oma_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OmaSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OmaSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingBase64".casefold():
            from .oma_setting_base64 import OmaSettingBase64

            return OmaSettingBase64()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingBoolean".casefold():
            from .oma_setting_boolean import OmaSettingBoolean

            return OmaSettingBoolean()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingDateTime".casefold():
            from .oma_setting_date_time import OmaSettingDateTime

            return OmaSettingDateTime()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingFloatingPoint".casefold():
            from .oma_setting_floating_point import OmaSettingFloatingPoint

            return OmaSettingFloatingPoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingInteger".casefold():
            from .oma_setting_integer import OmaSettingInteger

            return OmaSettingInteger()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingString".casefold():
            from .oma_setting_string import OmaSettingString

            return OmaSettingString()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingStringXml".casefold():
            from .oma_setting_string_xml import OmaSettingStringXml

            return OmaSettingStringXml()
        return OmaSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .oma_setting_base64 import OmaSettingBase64
        from .oma_setting_boolean import OmaSettingBoolean
        from .oma_setting_date_time import OmaSettingDateTime
        from .oma_setting_floating_point import OmaSettingFloatingPoint
        from .oma_setting_integer import OmaSettingInteger
        from .oma_setting_string import OmaSettingString
        from .oma_setting_string_xml import OmaSettingStringXml

        from .oma_setting_base64 import OmaSettingBase64
        from .oma_setting_boolean import OmaSettingBoolean
        from .oma_setting_date_time import OmaSettingDateTime
        from .oma_setting_floating_point import OmaSettingFloatingPoint
        from .oma_setting_integer import OmaSettingInteger
        from .oma_setting_string import OmaSettingString
        from .oma_setting_string_xml import OmaSettingStringXml

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "omaUri": lambda n : setattr(self, 'oma_uri', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("omaUri", self.oma_uri)
        writer.write_additional_data_value(self.additional_data)
    

