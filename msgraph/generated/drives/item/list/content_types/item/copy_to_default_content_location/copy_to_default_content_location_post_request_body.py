from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_reference = lazy_import('msgraph.generated.models.item_reference')

class CopyToDefaultContentLocationPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the copyToDefaultContentLocation method.
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
        Instantiates a new copyToDefaultContentLocationPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The destinationFileName property
        self._destination_file_name: Optional[str] = None
        # The sourceFile property
        self._source_file: Optional[item_reference.ItemReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyToDefaultContentLocationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CopyToDefaultContentLocationPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CopyToDefaultContentLocationPostRequestBody()
    
    @property
    def destination_file_name(self,) -> Optional[str]:
        """
        Gets the destinationFileName property value. The destinationFileName property
        Returns: Optional[str]
        """
        return self._destination_file_name
    
    @destination_file_name.setter
    def destination_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationFileName property value. The destinationFileName property
        Args:
            value: Value to set for the destinationFileName property.
        """
        self._destination_file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_file_name": lambda n : setattr(self, 'destination_file_name', n.get_str_value()),
            "source_file": lambda n : setattr(self, 'source_file', n.get_object_value(item_reference.ItemReference)),
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
        writer.write_str_value("destinationFileName", self.destination_file_name)
        writer.write_object_value("sourceFile", self.source_file)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_file(self,) -> Optional[item_reference.ItemReference]:
        """
        Gets the sourceFile property value. The sourceFile property
        Returns: Optional[item_reference.ItemReference]
        """
        return self._source_file
    
    @source_file.setter
    def source_file(self,value: Optional[item_reference.ItemReference] = None) -> None:
        """
        Sets the sourceFile property value. The sourceFile property
        Args:
            value: Value to set for the sourceFile property.
        """
        self._source_file = value
    

