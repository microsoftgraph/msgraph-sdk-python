from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AndroidMinimumOperatingSystem(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties for the minimum operating system required for an Android mobile app.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # When TRUE, only Version 10.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_0: Optional[bool] = None
    # When TRUE, only Version 11.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v11_0: Optional[bool] = None
    # When TRUE, only Version 4.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_0: Optional[bool] = None
    # When TRUE, only Version 4.0.3 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_0_3: Optional[bool] = None
    # When TRUE, only Version 4.1 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_1: Optional[bool] = None
    # When TRUE, only Version 4.2 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_2: Optional[bool] = None
    # When TRUE, only Version 4.3 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_3: Optional[bool] = None
    # When TRUE, only Version 4.4 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v4_4: Optional[bool] = None
    # When TRUE, only Version 5.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v5_0: Optional[bool] = None
    # When TRUE, only Version 5.1 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v5_1: Optional[bool] = None
    # When TRUE, only Version 6.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v6_0: Optional[bool] = None
    # When TRUE, only Version 7.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v7_0: Optional[bool] = None
    # When TRUE, only Version 7.1 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v7_1: Optional[bool] = None
    # When TRUE, only Version 8.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v8_0: Optional[bool] = None
    # When TRUE, only Version 8.1 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v8_1: Optional[bool] = None
    # When TRUE, only Version 9.0 or later is supported. Default value is FALSE. Exactly one of the minimum operating system boolean values will be TRUE.
    v9_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidMinimumOperatingSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v4_0": lambda n : setattr(self, 'v4_0', n.get_bool_value()),
            "v4_0_3": lambda n : setattr(self, 'v4_0_3', n.get_bool_value()),
            "v4_1": lambda n : setattr(self, 'v4_1', n.get_bool_value()),
            "v4_2": lambda n : setattr(self, 'v4_2', n.get_bool_value()),
            "v4_3": lambda n : setattr(self, 'v4_3', n.get_bool_value()),
            "v4_4": lambda n : setattr(self, 'v4_4', n.get_bool_value()),
            "v5_0": lambda n : setattr(self, 'v5_0', n.get_bool_value()),
            "v5_1": lambda n : setattr(self, 'v5_1', n.get_bool_value()),
            "v6_0": lambda n : setattr(self, 'v6_0', n.get_bool_value()),
            "v7_0": lambda n : setattr(self, 'v7_0', n.get_bool_value()),
            "v7_1": lambda n : setattr(self, 'v7_1', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v8_1": lambda n : setattr(self, 'v8_1', n.get_bool_value()),
            "v9_0": lambda n : setattr(self, 'v9_0', n.get_bool_value()),
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
        writer.write_bool_value("v10_0", self.v10_0)
        writer.write_bool_value("v11_0", self.v11_0)
        writer.write_bool_value("v4_0", self.v4_0)
        writer.write_bool_value("v4_0_3", self.v4_0_3)
        writer.write_bool_value("v4_1", self.v4_1)
        writer.write_bool_value("v4_2", self.v4_2)
        writer.write_bool_value("v4_3", self.v4_3)
        writer.write_bool_value("v4_4", self.v4_4)
        writer.write_bool_value("v5_0", self.v5_0)
        writer.write_bool_value("v5_1", self.v5_1)
        writer.write_bool_value("v6_0", self.v6_0)
        writer.write_bool_value("v7_0", self.v7_0)
        writer.write_bool_value("v7_1", self.v7_1)
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v8_1", self.v8_1)
        writer.write_bool_value("v9_0", self.v9_0)
        writer.write_additional_data_value(self.additional_data)
    

