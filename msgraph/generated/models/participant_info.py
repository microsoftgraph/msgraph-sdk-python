from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .endpoint_type import EndpointType
    from .identity_set import IdentitySet

@dataclass
class ParticipantInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.
    country_code: Optional[str] = None
    # The type of endpoint the participant is using. The possible values are: default, skypeForBusiness, or skypeForBusinessVoipPhone. Read-only.
    endpoint_type: Optional[EndpointType] = None
    # The identity property
    identity: Optional[IdentitySet] = None
    # The language culture string. Read-only.
    language_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participant ID of the participant. Read-only.
    participant_id: Optional[str] = None
    # The home region of the participant. This can be a country, a continent, or a larger geographic region. This doesn't change based on the participant's current physical location. Read-only.
    region: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParticipantInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ParticipantInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .endpoint_type import EndpointType
        from .identity_set import IdentitySet

        from .endpoint_type import EndpointType
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "endpointType": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(EndpointType)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(IdentitySet)),
            "languageId": lambda n : setattr(self, 'language_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("countryCode", self.country_code)
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("languageId", self.language_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("participantId", self.participant_id)
        writer.write_str_value("region", self.region)
        writer.write_additional_data_value(self.additional_data)
    

