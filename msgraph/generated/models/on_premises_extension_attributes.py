from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesExtensionAttributes(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # First customizable extension attribute.
    extension_attribute1: Optional[str] = None
    # Tenth customizable extension attribute.
    extension_attribute10: Optional[str] = None
    # Eleventh customizable extension attribute.
    extension_attribute11: Optional[str] = None
    # Twelfth customizable extension attribute.
    extension_attribute12: Optional[str] = None
    # Thirteenth customizable extension attribute.
    extension_attribute13: Optional[str] = None
    # Fourteenth customizable extension attribute.
    extension_attribute14: Optional[str] = None
    # Fifteenth customizable extension attribute.
    extension_attribute15: Optional[str] = None
    # Second customizable extension attribute.
    extension_attribute2: Optional[str] = None
    # Third customizable extension attribute.
    extension_attribute3: Optional[str] = None
    # Fourth customizable extension attribute.
    extension_attribute4: Optional[str] = None
    # Fifth customizable extension attribute.
    extension_attribute5: Optional[str] = None
    # Sixth customizable extension attribute.
    extension_attribute6: Optional[str] = None
    # Seventh customizable extension attribute.
    extension_attribute7: Optional[str] = None
    # Eighth customizable extension attribute.
    extension_attribute8: Optional[str] = None
    # Ninth customizable extension attribute.
    extension_attribute9: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesExtensionAttributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesExtensionAttributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesExtensionAttributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "extensionAttribute1": lambda n : setattr(self, 'extension_attribute1', n.get_str_value()),
            "extensionAttribute10": lambda n : setattr(self, 'extension_attribute10', n.get_str_value()),
            "extensionAttribute11": lambda n : setattr(self, 'extension_attribute11', n.get_str_value()),
            "extensionAttribute12": lambda n : setattr(self, 'extension_attribute12', n.get_str_value()),
            "extensionAttribute13": lambda n : setattr(self, 'extension_attribute13', n.get_str_value()),
            "extensionAttribute14": lambda n : setattr(self, 'extension_attribute14', n.get_str_value()),
            "extensionAttribute15": lambda n : setattr(self, 'extension_attribute15', n.get_str_value()),
            "extensionAttribute2": lambda n : setattr(self, 'extension_attribute2', n.get_str_value()),
            "extensionAttribute3": lambda n : setattr(self, 'extension_attribute3', n.get_str_value()),
            "extensionAttribute4": lambda n : setattr(self, 'extension_attribute4', n.get_str_value()),
            "extensionAttribute5": lambda n : setattr(self, 'extension_attribute5', n.get_str_value()),
            "extensionAttribute6": lambda n : setattr(self, 'extension_attribute6', n.get_str_value()),
            "extensionAttribute7": lambda n : setattr(self, 'extension_attribute7', n.get_str_value()),
            "extensionAttribute8": lambda n : setattr(self, 'extension_attribute8', n.get_str_value()),
            "extensionAttribute9": lambda n : setattr(self, 'extension_attribute9', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("extensionAttribute1", self.extension_attribute1)
        writer.write_str_value("extensionAttribute10", self.extension_attribute10)
        writer.write_str_value("extensionAttribute11", self.extension_attribute11)
        writer.write_str_value("extensionAttribute12", self.extension_attribute12)
        writer.write_str_value("extensionAttribute13", self.extension_attribute13)
        writer.write_str_value("extensionAttribute14", self.extension_attribute14)
        writer.write_str_value("extensionAttribute15", self.extension_attribute15)
        writer.write_str_value("extensionAttribute2", self.extension_attribute2)
        writer.write_str_value("extensionAttribute3", self.extension_attribute3)
        writer.write_str_value("extensionAttribute4", self.extension_attribute4)
        writer.write_str_value("extensionAttribute5", self.extension_attribute5)
        writer.write_str_value("extensionAttribute6", self.extension_attribute6)
        writer.write_str_value("extensionAttribute7", self.extension_attribute7)
        writer.write_str_value("extensionAttribute8", self.extension_attribute8)
        writer.write_str_value("extensionAttribute9", self.extension_attribute9)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

