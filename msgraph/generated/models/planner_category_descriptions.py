from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PlannerCategoryDescriptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The label associated with Category 1
    category1: Optional[str] = None
    # The label associated with Category 10
    category10: Optional[str] = None
    # The label associated with Category 11
    category11: Optional[str] = None
    # The label associated with Category 12
    category12: Optional[str] = None
    # The label associated with Category 13
    category13: Optional[str] = None
    # The label associated with Category 14
    category14: Optional[str] = None
    # The label associated with Category 15
    category15: Optional[str] = None
    # The label associated with Category 16
    category16: Optional[str] = None
    # The label associated with Category 17
    category17: Optional[str] = None
    # The label associated with Category 18
    category18: Optional[str] = None
    # The label associated with Category 19
    category19: Optional[str] = None
    # The label associated with Category 2
    category2: Optional[str] = None
    # The label associated with Category 20
    category20: Optional[str] = None
    # The label associated with Category 21
    category21: Optional[str] = None
    # The label associated with Category 22
    category22: Optional[str] = None
    # The label associated with Category 23
    category23: Optional[str] = None
    # The label associated with Category 24
    category24: Optional[str] = None
    # The label associated with Category 25
    category25: Optional[str] = None
    # The label associated with Category 3
    category3: Optional[str] = None
    # The label associated with Category 4
    category4: Optional[str] = None
    # The label associated with Category 5
    category5: Optional[str] = None
    # The label associated with Category 6
    category6: Optional[str] = None
    # The label associated with Category 7
    category7: Optional[str] = None
    # The label associated with Category 8
    category8: Optional[str] = None
    # The label associated with Category 9
    category9: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerCategoryDescriptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerCategoryDescriptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerCategoryDescriptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "category1": lambda n : setattr(self, 'category1', n.get_str_value()),
            "category10": lambda n : setattr(self, 'category10', n.get_str_value()),
            "category11": lambda n : setattr(self, 'category11', n.get_str_value()),
            "category12": lambda n : setattr(self, 'category12', n.get_str_value()),
            "category13": lambda n : setattr(self, 'category13', n.get_str_value()),
            "category14": lambda n : setattr(self, 'category14', n.get_str_value()),
            "category15": lambda n : setattr(self, 'category15', n.get_str_value()),
            "category16": lambda n : setattr(self, 'category16', n.get_str_value()),
            "category17": lambda n : setattr(self, 'category17', n.get_str_value()),
            "category18": lambda n : setattr(self, 'category18', n.get_str_value()),
            "category19": lambda n : setattr(self, 'category19', n.get_str_value()),
            "category2": lambda n : setattr(self, 'category2', n.get_str_value()),
            "category20": lambda n : setattr(self, 'category20', n.get_str_value()),
            "category21": lambda n : setattr(self, 'category21', n.get_str_value()),
            "category22": lambda n : setattr(self, 'category22', n.get_str_value()),
            "category23": lambda n : setattr(self, 'category23', n.get_str_value()),
            "category24": lambda n : setattr(self, 'category24', n.get_str_value()),
            "category25": lambda n : setattr(self, 'category25', n.get_str_value()),
            "category3": lambda n : setattr(self, 'category3', n.get_str_value()),
            "category4": lambda n : setattr(self, 'category4', n.get_str_value()),
            "category5": lambda n : setattr(self, 'category5', n.get_str_value()),
            "category6": lambda n : setattr(self, 'category6', n.get_str_value()),
            "category7": lambda n : setattr(self, 'category7', n.get_str_value()),
            "category8": lambda n : setattr(self, 'category8', n.get_str_value()),
            "category9": lambda n : setattr(self, 'category9', n.get_str_value()),
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
        writer.write_str_value("category1", self.category1)
        writer.write_str_value("category10", self.category10)
        writer.write_str_value("category11", self.category11)
        writer.write_str_value("category12", self.category12)
        writer.write_str_value("category13", self.category13)
        writer.write_str_value("category14", self.category14)
        writer.write_str_value("category15", self.category15)
        writer.write_str_value("category16", self.category16)
        writer.write_str_value("category17", self.category17)
        writer.write_str_value("category18", self.category18)
        writer.write_str_value("category19", self.category19)
        writer.write_str_value("category2", self.category2)
        writer.write_str_value("category20", self.category20)
        writer.write_str_value("category21", self.category21)
        writer.write_str_value("category22", self.category22)
        writer.write_str_value("category23", self.category23)
        writer.write_str_value("category24", self.category24)
        writer.write_str_value("category25", self.category25)
        writer.write_str_value("category3", self.category3)
        writer.write_str_value("category4", self.category4)
        writer.write_str_value("category5", self.category5)
        writer.write_str_value("category6", self.category6)
        writer.write_str_value("category7", self.category7)
        writer.write_str_value("category8", self.category8)
        writer.write_str_value("category9", self.category9)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

