from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')
initiator_type = lazy_import('msgraph.generated.models.initiator_type')

class Initiator(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new Initiator and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.initiator"
        # Type of initiator. Possible values are: user, application, system, unknownFutureValue.
        self._initiator_type: Optional[initiator_type.InitiatorType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Initiator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Initiator
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Initiator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "initiator_type": lambda n : setattr(self, 'initiator_type', n.get_enum_value(initiator_type.InitiatorType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator_type(self,) -> Optional[initiator_type.InitiatorType]:
        """
        Gets the initiatorType property value. Type of initiator. Possible values are: user, application, system, unknownFutureValue.
        Returns: Optional[initiator_type.InitiatorType]
        """
        return self._initiator_type
    
    @initiator_type.setter
    def initiator_type(self,value: Optional[initiator_type.InitiatorType] = None) -> None:
        """
        Sets the initiatorType property value. Type of initiator. Possible values are: user, application, system, unknownFutureValue.
        Args:
            value: Value to set for the initiatorType property.
        """
        self._initiator_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("initiatorType", self.initiator_type)
    

