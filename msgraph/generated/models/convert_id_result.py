from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

generic_error = lazy_import('msgraph.generated.models.generic_error')

class ConvertIdResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new convertIdResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # An error object indicating the reason for the conversion failure. This value is not present if the conversion succeeded.
        self._error_details: Optional[generic_error.GenericError] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identifier that was converted. This value is the original, un-converted identifier.
        self._source_id: Optional[str] = None
        # The converted identifier. This value is not present if the conversion failed.
        self._target_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConvertIdResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConvertIdResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConvertIdResult()
    
    @property
    def error_details(self,) -> Optional[generic_error.GenericError]:
        """
        Gets the errorDetails property value. An error object indicating the reason for the conversion failure. This value is not present if the conversion succeeded.
        Returns: Optional[generic_error.GenericError]
        """
        return self._error_details
    
    @error_details.setter
    def error_details(self,value: Optional[generic_error.GenericError] = None) -> None:
        """
        Sets the errorDetails property value. An error object indicating the reason for the conversion failure. This value is not present if the conversion succeeded.
        Args:
            value: Value to set for the errorDetails property.
        """
        self._error_details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error_details": lambda n : setattr(self, 'error_details', n.get_object_value(generic_error.GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_id": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "target_id": lambda n : setattr(self, 'target_id', n.get_str_value()),
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
        writer.write_object_value("errorDetails", self.error_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("targetId", self.target_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. The identifier that was converted. This value is the original, un-converted identifier.
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. The identifier that was converted. This value is the original, un-converted identifier.
        Args:
            value: Value to set for the sourceId property.
        """
        self._source_id = value
    
    @property
    def target_id(self,) -> Optional[str]:
        """
        Gets the targetId property value. The converted identifier. This value is not present if the conversion failed.
        Returns: Optional[str]
        """
        return self._target_id
    
    @target_id.setter
    def target_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetId property value. The converted identifier. This value is not present if the conversion failed.
        Args:
            value: Value to set for the targetId property.
        """
        self._target_id = value
    

