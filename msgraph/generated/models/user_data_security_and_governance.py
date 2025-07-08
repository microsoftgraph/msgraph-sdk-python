from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activities_container import ActivitiesContainer
    from .data_security_and_governance import DataSecurityAndGovernance
    from .user_protection_scope_container import UserProtectionScopeContainer

from .data_security_and_governance import DataSecurityAndGovernance

@dataclass
class UserDataSecurityAndGovernance(DataSecurityAndGovernance, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userDataSecurityAndGovernance"
    # Container for activity logs (content processing and audit) related to this user. ContainsTarget: true.
    activities: Optional[ActivitiesContainer] = None
    # The protectionScopes property
    protection_scopes: Optional[UserProtectionScopeContainer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserDataSecurityAndGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserDataSecurityAndGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserDataSecurityAndGovernance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activities_container import ActivitiesContainer
        from .data_security_and_governance import DataSecurityAndGovernance
        from .user_protection_scope_container import UserProtectionScopeContainer

        from .activities_container import ActivitiesContainer
        from .data_security_and_governance import DataSecurityAndGovernance
        from .user_protection_scope_container import UserProtectionScopeContainer

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_object_value(ActivitiesContainer)),
            "protectionScopes": lambda n : setattr(self, 'protection_scopes', n.get_object_value(UserProtectionScopeContainer)),
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
        writer.write_object_value("activities", self.activities)
        writer.write_object_value("protectionScopes", self.protection_scopes)
    

