from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .terms_and_conditions import TermsAndConditions

from .entity import Entity

@dataclass
class TermsAndConditionsAcceptanceStatus(Entity, Parsable):
    """
    A termsAndConditionsAcceptanceStatus entity represents the acceptance status of a given Terms and Conditions (T&C) policy by a given user. Users must accept the most up-to-date version of the terms in order to retain access to the Company Portal.
    """
    # DateTime when the terms were last accepted by the user.
    accepted_date_time: Optional[datetime.datetime] = None
    # Most recent version number of the T&C accepted by the user.
    accepted_version: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Navigation link to the terms and conditions that are assigned.
    terms_and_conditions: Optional[TermsAndConditions] = None
    # Display name of the user whose acceptance the entity represents.
    user_display_name: Optional[str] = None
    # The userPrincipalName of the User that accepted the term.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TermsAndConditionsAcceptanceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditionsAcceptanceStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TermsAndConditionsAcceptanceStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .terms_and_conditions import TermsAndConditions

        from .entity import Entity
        from .terms_and_conditions import TermsAndConditions

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedDateTime": lambda n : setattr(self, 'accepted_date_time', n.get_datetime_value()),
            "acceptedVersion": lambda n : setattr(self, 'accepted_version', n.get_int_value()),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_object_value(TermsAndConditions)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
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
        writer.write_datetime_value("acceptedDateTime", self.accepted_date_time)
        writer.write_int_value("acceptedVersion", self.accepted_version)
        writer.write_object_value("termsAndConditions", self.terms_and_conditions)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

