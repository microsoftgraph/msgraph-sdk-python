from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CheckMemberGroupsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the checkMemberGroups method.
    """
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
        Instantiates a new checkMemberGroupsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupIds property
        self._group_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CheckMemberGroupsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CheckMemberGroupsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CheckMemberGroupsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_ids": lambda n : setattr(self, 'group_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def group_ids(self,) -> Optional[List[str]]:
        """
        Gets the groupIds property value. The groupIds property
        Returns: Optional[List[str]]
        """
        return self._group_ids
    
    @group_ids.setter
    def group_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the groupIds property value. The groupIds property
        Args:
            value: Value to set for the groupIds property.
        """
        self._group_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("groupIds", self.group_ids)
        writer.write_additional_data_value(self.additional_data)
    

