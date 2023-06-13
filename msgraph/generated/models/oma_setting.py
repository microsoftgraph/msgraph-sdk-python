from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import oma_setting_base64, oma_setting_boolean, oma_setting_date_time, oma_setting_floating_point, oma_setting_integer, oma_setting_string, oma_setting_string_xml

@dataclass
class OmaSetting(AdditionalDataHolder, Parsable):
    """
    OMA Settings definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Description.
    description: Optional[str] = None
    # Display Name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OMA.
    oma_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.omaSettingBase64":
                from . import oma_setting_base64

                return oma_setting_base64.OmaSettingBase64()
            if mapping_value == "#microsoft.graph.omaSettingBoolean":
                from . import oma_setting_boolean

                return oma_setting_boolean.OmaSettingBoolean()
            if mapping_value == "#microsoft.graph.omaSettingDateTime":
                from . import oma_setting_date_time

                return oma_setting_date_time.OmaSettingDateTime()
            if mapping_value == "#microsoft.graph.omaSettingFloatingPoint":
                from . import oma_setting_floating_point

                return oma_setting_floating_point.OmaSettingFloatingPoint()
            if mapping_value == "#microsoft.graph.omaSettingInteger":
                from . import oma_setting_integer

                return oma_setting_integer.OmaSettingInteger()
            if mapping_value == "#microsoft.graph.omaSettingString":
                from . import oma_setting_string

                return oma_setting_string.OmaSettingString()
            if mapping_value == "#microsoft.graph.omaSettingStringXml":
                from . import oma_setting_string_xml

                return oma_setting_string_xml.OmaSettingStringXml()
        return OmaSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import oma_setting_base64, oma_setting_boolean, oma_setting_date_time, oma_setting_floating_point, oma_setting_integer, oma_setting_string, oma_setting_string_xml

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "omaUri": lambda n : setattr(self, 'oma_uri', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("omaUri", self.oma_uri)
        writer.write_additional_data_value(self.additional_data)
    

