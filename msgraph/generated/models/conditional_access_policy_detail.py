from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_condition_set import ConditionalAccessConditionSet
    from .conditional_access_grant_controls import ConditionalAccessGrantControls
    from .conditional_access_session_controls import ConditionalAccessSessionControls

@dataclass
class ConditionalAccessPolicyDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The conditions property
    conditions: Optional[ConditionalAccessConditionSet] = None
    # Represents grant controls that must be fulfilled for the policy.
    grant_controls: Optional[ConditionalAccessGrantControls] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a complex type of session controls that is enforced after sign-in.
    session_controls: Optional[ConditionalAccessSessionControls] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessPolicyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicyDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessPolicyDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_condition_set import ConditionalAccessConditionSet
        from .conditional_access_grant_controls import ConditionalAccessGrantControls
        from .conditional_access_session_controls import ConditionalAccessSessionControls

        from .conditional_access_condition_set import ConditionalAccessConditionSet
        from .conditional_access_grant_controls import ConditionalAccessGrantControls
        from .conditional_access_session_controls import ConditionalAccessSessionControls

        fields: dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(ConditionalAccessConditionSet)),
            "grantControls": lambda n : setattr(self, 'grant_controls', n.get_object_value(ConditionalAccessGrantControls)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sessionControls": lambda n : setattr(self, 'session_controls', n.get_object_value(ConditionalAccessSessionControls)),
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
        writer.write_object_value("conditions", self.conditions)
        writer.write_object_value("grantControls", self.grant_controls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sessionControls", self.session_controls)
        writer.write_additional_data_value(self.additional_data)
    

