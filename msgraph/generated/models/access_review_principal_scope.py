from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_principal_scope_type import AccessReviewPrincipalScopeType
    from .access_review_scope import AccessReviewScope

from .access_review_scope import AccessReviewScope

@dataclass
class AccessReviewPrincipalScope(AccessReviewScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewPrincipalScope"
    # The scopeType property
    scope_type: Optional[AccessReviewPrincipalScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewPrincipalScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewPrincipalScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewPrincipalScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_principal_scope_type import AccessReviewPrincipalScopeType
        from .access_review_scope import AccessReviewScope

        from .access_review_principal_scope_type import AccessReviewPrincipalScopeType
        from .access_review_scope import AccessReviewScope

        fields: dict[str, Callable[[Any], None]] = {
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_enum_value(AccessReviewPrincipalScopeType)),
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
        writer.write_enum_value("scopeType", self.scope_type)
    

