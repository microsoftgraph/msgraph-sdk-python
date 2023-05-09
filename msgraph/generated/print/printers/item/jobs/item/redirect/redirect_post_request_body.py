from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import print_job_configuration

class RedirectPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new redirectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The configuration property
        self._configuration: Optional[print_job_configuration.PrintJobConfiguration] = None
        # The destinationPrinterId property
        self._destination_printer_id: Optional[str] = None
    
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
    
    @property
    def configuration(self,) -> Optional[print_job_configuration.PrintJobConfiguration]:
        """
        Gets the configuration property value. The configuration property
        Returns: Optional[print_job_configuration.PrintJobConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[print_job_configuration.PrintJobConfiguration] = None) -> None:
        """
        Sets the configuration property value. The configuration property
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedirectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RedirectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RedirectPostRequestBody()
    
    @property
    def destination_printer_id(self,) -> Optional[str]:
        """
        Gets the destinationPrinterId property value. The destinationPrinterId property
        Returns: Optional[str]
        """
        return self._destination_printer_id
    
    @destination_printer_id.setter
    def destination_printer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationPrinterId property value. The destinationPrinterId property
        Args:
            value: Value to set for the destination_printer_id property.
        """
        self._destination_printer_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import print_job_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(print_job_configuration.PrintJobConfiguration)),
            "destinationPrinterId": lambda n : setattr(self, 'destination_printer_id', n.get_str_value()),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("destinationPrinterId", self.destination_printer_id)
        writer.write_additional_data_value(self.additional_data)
    

