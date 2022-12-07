from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

pending_content_update = lazy_import('msgraph.generated.models.pending_content_update')

class PendingOperations(AdditionalDataHolder, Parsable):
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
        Instantiates a new pendingOperations and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # A property that indicates that an operation that might update the binary content of a file is pending completion.
        self._pending_content_update: Optional[pending_content_update.PendingContentUpdate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PendingOperations:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PendingOperations
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PendingOperations()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pending_content_update": lambda n : setattr(self, 'pending_content_update', n.get_object_value(pending_content_update.PendingContentUpdate)),
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
    
    @property
    def pending_content_update(self,) -> Optional[pending_content_update.PendingContentUpdate]:
        """
        Gets the pendingContentUpdate property value. A property that indicates that an operation that might update the binary content of a file is pending completion.
        Returns: Optional[pending_content_update.PendingContentUpdate]
        """
        return self._pending_content_update
    
    @pending_content_update.setter
    def pending_content_update(self,value: Optional[pending_content_update.PendingContentUpdate] = None) -> None:
        """
        Sets the pendingContentUpdate property value. A property that indicates that an operation that might update the binary content of a file is pending completion.
        Args:
            value: Value to set for the pendingContentUpdate property.
        """
        self._pending_content_update = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("pendingContentUpdate", self.pending_content_update)
        writer.write_additional_data_value(self.additional_data)
    

