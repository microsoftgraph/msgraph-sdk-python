from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .included_user_roles import IncludedUserRoles
    from .included_user_types import IncludedUserTypes
    from .user_registration_feature_count import UserRegistrationFeatureCount

@dataclass
class UserRegistrationFeatureSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Total number of users accounts, excluding those that are blocked.
    total_user_count: Optional[int] = None
    # Number of users registered or capable for multi-factor authentication, self-service password reset, and passwordless authentication.
    user_registration_feature_counts: Optional[list[UserRegistrationFeatureCount]] = None
    # The role type of the user. The possible values are: all, privilegedAdmin, admin, user, unknownFutureValue.
    user_roles: Optional[IncludedUserRoles] = None
    # User type. The possible values are: all, member, guest, unknownFutureValue.
    user_types: Optional[IncludedUserTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserRegistrationFeatureSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationFeatureSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserRegistrationFeatureSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .included_user_roles import IncludedUserRoles
        from .included_user_types import IncludedUserTypes
        from .user_registration_feature_count import UserRegistrationFeatureCount

        from .included_user_roles import IncludedUserRoles
        from .included_user_types import IncludedUserTypes
        from .user_registration_feature_count import UserRegistrationFeatureCount

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalUserCount": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
            "userRegistrationFeatureCounts": lambda n : setattr(self, 'user_registration_feature_counts', n.get_collection_of_object_values(UserRegistrationFeatureCount)),
            "userRoles": lambda n : setattr(self, 'user_roles', n.get_enum_value(IncludedUserRoles)),
            "userTypes": lambda n : setattr(self, 'user_types', n.get_enum_value(IncludedUserTypes)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalUserCount", self.total_user_count)
        writer.write_collection_of_object_values("userRegistrationFeatureCounts", self.user_registration_feature_counts)
        writer.write_enum_value("userRoles", self.user_roles)
        writer.write_enum_value("userTypes", self.user_types)
        writer.write_additional_data_value(self.additional_data)
    

