from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..user import User
    from .account_type import AccountType
    from .assigned_telephone_number import AssignedTelephoneNumber
    from .effective_policy_assignment import EffectivePolicyAssignment

from ..entity import Entity

@dataclass
class TeamsUserConfiguration(Entity, Parsable):
    # The accountType property
    account_type: Optional[AccountType] = None
    # The date and time when the user was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Contains the user's effective policy assignments, with each assignment including policyType and policyAssignment details.
    effective_policy_assignments: Optional[list[EffectivePolicyAssignment]] = None
    # The Teams features enabled for a given user based on licensing or service plan.
    feature_types: Optional[list[str]] = None
    # Indicates whether voice capability is enabled.
    is_enterprise_voice_enabled: Optional[bool] = None
    # The date and time when the user's details were last modified. The system updates this value each time the user's details are changed. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Includes both the phone number and its corresponding assignment category. The assignment category can include values such as primary, private, and alternate.
    telephone_numbers: Optional[list[AssignedTelephoneNumber]] = None
    # The unique identifier of the tenant in Entra to which this user is assigned.
    tenant_id: Optional[str] = None
    # Represents an Entra user account.
    user: Optional[User] = None
    # The sign-in address of the user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsUserConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsUserConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsUserConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..user import User
        from .account_type import AccountType
        from .assigned_telephone_number import AssignedTelephoneNumber
        from .effective_policy_assignment import EffectivePolicyAssignment

        from ..entity import Entity
        from ..user import User
        from .account_type import AccountType
        from .assigned_telephone_number import AssignedTelephoneNumber
        from .effective_policy_assignment import EffectivePolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "accountType": lambda n : setattr(self, 'account_type', n.get_enum_value(AccountType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "effectivePolicyAssignments": lambda n : setattr(self, 'effective_policy_assignments', n.get_collection_of_object_values(EffectivePolicyAssignment)),
            "featureTypes": lambda n : setattr(self, 'feature_types', n.get_collection_of_primitive_values(str)),
            "isEnterpriseVoiceEnabled": lambda n : setattr(self, 'is_enterprise_voice_enabled', n.get_bool_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "telephoneNumbers": lambda n : setattr(self, 'telephone_numbers', n.get_collection_of_object_values(AssignedTelephoneNumber)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(User)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("accountType", self.account_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("effectivePolicyAssignments", self.effective_policy_assignments)
        writer.write_collection_of_primitive_values("featureTypes", self.feature_types)
        writer.write_bool_value("isEnterpriseVoiceEnabled", self.is_enterprise_voice_enabled)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_collection_of_object_values("telephoneNumbers", self.telephone_numbers)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

