from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..device_platform_type import DevicePlatformType

@dataclass
class AnswerVariant(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The answer variation description that is shown on the search results page.
    description: Optional[str] = None
    # The answer variation name that is displayed in search results.
    display_name: Optional[str] = None
    # The country or region that can view this answer variation.
    language_tag: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The device or operating system that can view this answer variation. Possible values are: android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, unknown, androidASOP, androidMobileApplicationManagement, iOSMobileApplicationManagement, unknownFutureValue.
    platform: Optional[DevicePlatformType] = None
    # The URL link for the answer variation. When users select this answer variation from the search results, they're directed to the specified URL.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnswerVariant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnswerVariant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnswerVariant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..device_platform_type import DevicePlatformType

        from ..device_platform_type import DevicePlatformType

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(DevicePlatformType)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

