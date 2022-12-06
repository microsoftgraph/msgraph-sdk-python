from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ItemActionStat(AdditionalDataHolder, Parsable):
    @property
    def action_count(self,) -> Optional[int]:
        """
        Gets the actionCount property value. The number of times the action took place. Read-only.
        Returns: Optional[int]
        """
        return self._action_count
    
    @action_count.setter
    def action_count(self,value: Optional[int] = None) -> None:
        """
        Sets the actionCount property value. The number of times the action took place. Read-only.
        Args:
            value: Value to set for the actionCount property.
        """
        self._action_count = value
    
    @property
    def actor_count(self,) -> Optional[int]:
        """
        Gets the actorCount property value. The number of distinct actors that performed the action. Read-only.
        Returns: Optional[int]
        """
        return self._actor_count
    
    @actor_count.setter
    def actor_count(self,value: Optional[int] = None) -> None:
        """
        Sets the actorCount property value. The number of distinct actors that performed the action. Read-only.
        Args:
            value: Value to set for the actorCount property.
        """
        self._actor_count = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemActionStat and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of times the action took place. Read-only.
        self._action_count: Optional[int] = None
        # The number of distinct actors that performed the action. Read-only.
        self._actor_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActionStat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActionStat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActionStat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_count": lambda n : setattr(self, 'action_count', n.get_int_value()),
            "actor_count": lambda n : setattr(self, 'actor_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("actionCount", self.action_count)
        writer.write_int_value("actorCount", self.actor_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

