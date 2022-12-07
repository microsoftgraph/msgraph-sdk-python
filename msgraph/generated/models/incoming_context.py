from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')

class IncomingContext(AdditionalDataHolder, Parsable):
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
        Instantiates a new incomingContext and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ID of the participant that is under observation. Read-only.
        self._observed_participant_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identity that the call is happening on behalf of.
        self._on_behalf_of: Optional[identity_set.IdentitySet] = None
        # The ID of the participant that triggered the incoming call. Read-only.
        self._source_participant_id: Optional[str] = None
        # The identity that transferred the call.
        self._transferor: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IncomingContext:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IncomingContext
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IncomingContext()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "observed_participant_id": lambda n : setattr(self, 'observed_participant_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_behalf_of": lambda n : setattr(self, 'on_behalf_of', n.get_object_value(identity_set.IdentitySet)),
            "source_participant_id": lambda n : setattr(self, 'source_participant_id', n.get_str_value()),
            "transferor": lambda n : setattr(self, 'transferor', n.get_object_value(identity_set.IdentitySet)),
        }
        return fields
    
    @property
    def observed_participant_id(self,) -> Optional[str]:
        """
        Gets the observedParticipantId property value. The ID of the participant that is under observation. Read-only.
        Returns: Optional[str]
        """
        return self._observed_participant_id
    
    @observed_participant_id.setter
    def observed_participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the observedParticipantId property value. The ID of the participant that is under observation. Read-only.
        Args:
            value: Value to set for the observedParticipantId property.
        """
        self._observed_participant_id = value
    
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
    def on_behalf_of(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the onBehalfOf property value. The identity that the call is happening on behalf of.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._on_behalf_of
    
    @on_behalf_of.setter
    def on_behalf_of(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the onBehalfOf property value. The identity that the call is happening on behalf of.
        Args:
            value: Value to set for the onBehalfOf property.
        """
        self._on_behalf_of = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("observedParticipantId", self.observed_participant_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("onBehalfOf", self.on_behalf_of)
        writer.write_str_value("sourceParticipantId", self.source_participant_id)
        writer.write_object_value("transferor", self.transferor)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_participant_id(self,) -> Optional[str]:
        """
        Gets the sourceParticipantId property value. The ID of the participant that triggered the incoming call. Read-only.
        Returns: Optional[str]
        """
        return self._source_participant_id
    
    @source_participant_id.setter
    def source_participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceParticipantId property value. The ID of the participant that triggered the incoming call. Read-only.
        Args:
            value: Value to set for the sourceParticipantId property.
        """
        self._source_participant_id = value
    
    @property
    def transferor(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the transferor property value. The identity that transferred the call.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._transferor
    
    @transferor.setter
    def transferor(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the transferor property value. The identity that transferred the call.
        Args:
            value: Value to set for the transferor property.
        """
        self._transferor = value
    

