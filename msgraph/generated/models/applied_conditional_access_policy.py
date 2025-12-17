from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult

@dataclass
class AppliedConditionalAccessPolicy(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Refers to the name of the conditional access policy (example: 'Require MFA for Salesforce').
    display_name: Optional[str] = None
    # Refers to the grant controls enforced by the conditional access policy (example: 'Require multifactor authentication').
    enforced_grant_controls: Optional[list[str]] = None
    # Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
    enforced_session_controls: Optional[list[str]] = None
    # An identifier of the conditional access policy. Supports $filter (eq).
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the result of the CA policy that was triggered. The possible values are: success, failure, notApplied (policy isn't applied because policy conditions weren't met), notEnabled (This is due to the policy in a disabled state), unknown, unknownFutureValue, reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted.
    result: Optional[AppliedConditionalAccessPolicyResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppliedConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppliedConditionalAccessPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppliedConditionalAccessPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult

        from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforcedGrantControls": lambda n : setattr(self, 'enforced_grant_controls', n.get_collection_of_primitive_values(str)),
            "enforcedSessionControls": lambda n : setattr(self, 'enforced_session_controls', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(AppliedConditionalAccessPolicyResult)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("enforcedGrantControls", self.enforced_grant_controls)
        writer.write_collection_of_primitive_values("enforcedSessionControls", self.enforced_session_controls)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("result", self.result)
        writer.write_additional_data_value(self.additional_data)
    

