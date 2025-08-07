from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.sign_in_conditions import SignInConditions
    from ....models.sign_in_context import SignInContext
    from ....models.sign_in_identity import SignInIdentity

@dataclass
class EvaluatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appliedPoliciesOnly property
    applied_policies_only: Optional[bool] = None
    # The signInConditions property
    sign_in_conditions: Optional[SignInConditions] = None
    # The signInContext property
    sign_in_context: Optional[SignInContext] = None
    # The signInIdentity property
    sign_in_identity: Optional[SignInIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluatePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.sign_in_conditions import SignInConditions
        from ....models.sign_in_context import SignInContext
        from ....models.sign_in_identity import SignInIdentity

        from ....models.sign_in_conditions import SignInConditions
        from ....models.sign_in_context import SignInContext
        from ....models.sign_in_identity import SignInIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "appliedPoliciesOnly": lambda n : setattr(self, 'applied_policies_only', n.get_bool_value()),
            "signInConditions": lambda n : setattr(self, 'sign_in_conditions', n.get_object_value(SignInConditions)),
            "signInContext": lambda n : setattr(self, 'sign_in_context', n.get_object_value(SignInContext)),
            "signInIdentity": lambda n : setattr(self, 'sign_in_identity', n.get_object_value(SignInIdentity)),
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
        writer.write_bool_value("appliedPoliciesOnly", self.applied_policies_only)
        writer.write_object_value("signInConditions", self.sign_in_conditions)
        writer.write_object_value("signInContext", self.sign_in_context)
        writer.write_object_value("signInIdentity", self.sign_in_identity)
        writer.write_additional_data_value(self.additional_data)
    

