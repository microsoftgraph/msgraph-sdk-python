from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MacOSMinimumOperatingSystem(AdditionalDataHolder, BackedModel, Parsable):
    """
    The minimum operating system required for a macOS app.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.10 or later is required to install the app. If 'False', OS X Version 10.10 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_10: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.11 or later is required to install the app. If 'False', OS X Version 10.11 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_11: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.12 or later is required to install the app. If 'False', OS X Version 10.12 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_12: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.13 or later is required to install the app. If 'False', OS X Version 10.13 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_13: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.14 or later is required to install the app. If 'False', OS X Version 10.14 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_14: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.15 or later is required to install the app. If 'False', OS X Version 10.15 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_15: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.7 or later is required to install the app. If 'False', OS X Version 10.7 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_7: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.8 or later is required to install the app. If 'False', OS X Version 10.8 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_8: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 10.9 or later is required to install the app. If 'False', OS X Version 10.9 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_9: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 11.0 or later is required to install the app. If 'False', OS X Version 11.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v11_0: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 12.0 or later is required to install the app. If 'False', OS X Version 12.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v12_0: Optional[bool] = None
    # Indicates the minimum OS X version support required for the managed device. When 'True', macOS with OS X 13.0 or later is required to install the app. If 'False', OS X Version 13.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v13_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSMinimumOperatingSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_10": lambda n : setattr(self, 'v10_10', n.get_bool_value()),
            "v10_11": lambda n : setattr(self, 'v10_11', n.get_bool_value()),
            "v10_12": lambda n : setattr(self, 'v10_12', n.get_bool_value()),
            "v10_13": lambda n : setattr(self, 'v10_13', n.get_bool_value()),
            "v10_14": lambda n : setattr(self, 'v10_14', n.get_bool_value()),
            "v10_15": lambda n : setattr(self, 'v10_15', n.get_bool_value()),
            "v10_7": lambda n : setattr(self, 'v10_7', n.get_bool_value()),
            "v10_8": lambda n : setattr(self, 'v10_8', n.get_bool_value()),
            "v10_9": lambda n : setattr(self, 'v10_9', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v12_0": lambda n : setattr(self, 'v12_0', n.get_bool_value()),
            "v13_0": lambda n : setattr(self, 'v13_0', n.get_bool_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("v10_10", self.v10_10)
        writer.write_bool_value("v10_11", self.v10_11)
        writer.write_bool_value("v10_12", self.v10_12)
        writer.write_bool_value("v10_13", self.v10_13)
        writer.write_bool_value("v10_14", self.v10_14)
        writer.write_bool_value("v10_15", self.v10_15)
        writer.write_bool_value("v10_7", self.v10_7)
        writer.write_bool_value("v10_8", self.v10_8)
        writer.write_bool_value("v10_9", self.v10_9)
        writer.write_bool_value("v11_0", self.v11_0)
        writer.write_bool_value("v12_0", self.v12_0)
        writer.write_bool_value("v13_0", self.v13_0)
        writer.write_additional_data_value(self.additional_data)
    

