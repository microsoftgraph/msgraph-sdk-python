from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_activity
    from .. import public_error

from . import external_activity

class ExternalActivityResult(external_activity.ExternalActivity):
    def __init__(self,) -> None:
        """
        Instantiates a new ExternalActivityResult and sets the default values.
        """
        super().__init__()
        # Error information that explains the failure to process an external activity.
        self._error: Optional[public_error.PublicError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalActivityResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalActivityResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalActivityResult()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. Error information that explains the failure to process an external activity.
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. Error information that explains the failure to process an external activity.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_activity
        from .. import public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("error", self.error)
    

