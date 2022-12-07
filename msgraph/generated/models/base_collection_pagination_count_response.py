from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BaseCollectionPaginationCountResponse(AdditionalDataHolder, Parsable):
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
        Instantiates a new BaseCollectionPaginationCountResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataCount property
        self._odata_count: Optional[int] = None
        # The OdataNextLink property
        self._odata_next_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseCollectionPaginationCountResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseCollectionPaginationCountResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BaseCollectionPaginationCountResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.count": lambda n : setattr(self, 'odata_count', n.get_int_value()),
            "@odata.nextLink": lambda n : setattr(self, 'odata_next_link', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_count(self,) -> Optional[int]:
        """
        Gets the @odata.count property value. The OdataCount property
        Returns: Optional[int]
        """
        return self._odata_count
    
    @odata_count.setter
    def odata_count(self,value: Optional[int] = None) -> None:
        """
        Sets the @odata.count property value. The OdataCount property
        Args:
            value: Value to set for the OdataCount property.
        """
        self._odata_count = value
    
    @property
    def odata_next_link(self,) -> Optional[str]:
        """
        Gets the @odata.nextLink property value. The OdataNextLink property
        Returns: Optional[str]
        """
        return self._odata_next_link
    
    @odata_next_link.setter
    def odata_next_link(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.nextLink property value. The OdataNextLink property
        Args:
            value: Value to set for the OdataNextLink property.
        """
        self._odata_next_link = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("@odata.count", self.odata_count)
        writer.write_str_value("@odata.nextLink", self.odata_next_link)
        writer.write_additional_data_value(self.additional_data)
    

