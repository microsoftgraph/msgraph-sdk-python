from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
    from .identity_user_flow_attribute import IdentityUserFlowAttribute
    from .on_attribute_collection_handler import OnAttributeCollectionHandler

from .on_attribute_collection_handler import OnAttributeCollectionHandler

@dataclass
class OnAttributeCollectionExternalUsersSelfServiceSignUp(OnAttributeCollectionHandler):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp"
    # Required. The configuration for how attributes are displayed in the sign up experience defined by a user flow, like the externalUsersSelfServiceSignupEventsFlow, specifically on the attribute collection page.
    attribute_collection_page: Optional[AuthenticationAttributeCollectionPage] = None
    # The attributes property
    attributes: Optional[List[IdentityUserFlowAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnAttributeCollectionExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnAttributeCollectionExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnAttributeCollectionExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .on_attribute_collection_handler import OnAttributeCollectionHandler

        from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .on_attribute_collection_handler import OnAttributeCollectionHandler

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeCollectionPage": lambda n : setattr(self, 'attribute_collection_page', n.get_object_value(AuthenticationAttributeCollectionPage)),
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(IdentityUserFlowAttribute)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("attributeCollectionPage", self.attribute_collection_page)
        writer.write_collection_of_object_values("attributes", self.attributes)
    

