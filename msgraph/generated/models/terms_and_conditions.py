from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
    from .terms_and_conditions_assignment import TermsAndConditionsAssignment

from .entity import Entity

@dataclass
class TermsAndConditions(Entity, Parsable):
    """
    A termsAndConditions entity represents the metadata and contents of a given Terms and Conditions (T&C) policy. T&C policies’ contents are presented to users upon their first attempt to enroll into Intune and subsequently upon edits where an administrator has required re-acceptance. They enable administrators to communicate the provisions to which a user must agree in order to have devices enrolled into Intune.
    """
    # Administrator-supplied explanation of the terms and conditions, typically describing what it means to accept the terms and conditions set out in the T&C policy. This is shown to the user on prompts to accept the T&C policy.
    acceptance_statement: Optional[str] = None
    # The list of acceptance statuses for this T&C policy.
    acceptance_statuses: Optional[list[TermsAndConditionsAcceptanceStatus]] = None
    # The list of assignments for this T&C policy.
    assignments: Optional[list[TermsAndConditionsAssignment]] = None
    # Administrator-supplied body text of the terms and conditions, typically the terms themselves. This is shown to the user on prompts to accept the T&C policy.
    body_text: Optional[str] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Administrator-supplied description of the T&C policy.
    description: Optional[str] = None
    # Administrator-supplied name for the T&C policy.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Administrator-supplied title of the terms and conditions. This is shown to the user on prompts to accept the T&C policy.
    title: Optional[str] = None
    # Integer indicating the current version of the terms. Incremented when an administrator makes a change to the terms and wishes to require users to re-accept the modified T&C policy.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TermsAndConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TermsAndConditions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment

        from .entity import Entity
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "acceptanceStatement": lambda n : setattr(self, 'acceptance_statement', n.get_str_value()),
            "acceptanceStatuses": lambda n : setattr(self, 'acceptance_statuses', n.get_collection_of_object_values(TermsAndConditionsAcceptanceStatus)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TermsAndConditionsAssignment)),
            "bodyText": lambda n : setattr(self, 'body_text', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_str_value("acceptanceStatement", self.acceptance_statement)
        writer.write_collection_of_object_values("acceptanceStatuses", self.acceptance_statuses)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("bodyText", self.body_text)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("title", self.title)
        writer.write_int_value("version", self.version)
    

