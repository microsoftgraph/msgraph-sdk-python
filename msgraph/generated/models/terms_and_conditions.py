from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, terms_and_conditions_acceptance_status, terms_and_conditions_assignment

from . import entity

class TermsAndConditions(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new termsAndConditions and sets the default values.
        """
        super().__init__()
        # Administrator-supplied explanation of the terms and conditions, typically describing what it means to accept the terms and conditions set out in the T&C policy. This is shown to the user on prompts to accept the T&C policy.
        self._acceptance_statement: Optional[str] = None
        # The list of acceptance statuses for this T&C policy.
        self._acceptance_statuses: Optional[List[terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus]] = None
        # The list of assignments for this T&C policy.
        self._assignments: Optional[List[terms_and_conditions_assignment.TermsAndConditionsAssignment]] = None
        # Administrator-supplied body text of the terms and conditions, typically the terms themselves. This is shown to the user on prompts to accept the T&C policy.
        self._body_text: Optional[str] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Administrator-supplied description of the T&C policy.
        self._description: Optional[str] = None
        # Administrator-supplied name for the T&C policy.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Administrator-supplied title of the terms and conditions. This is shown to the user on prompts to accept the T&C policy.
        self._title: Optional[str] = None
        # Integer indicating the current version of the terms. Incremented when an administrator makes a change to the terms and wishes to require users to re-accept the modified T&C policy.
        self._version: Optional[int] = None
    
    @property
    def acceptance_statement(self,) -> Optional[str]:
        """
        Gets the acceptanceStatement property value. Administrator-supplied explanation of the terms and conditions, typically describing what it means to accept the terms and conditions set out in the T&C policy. This is shown to the user on prompts to accept the T&C policy.
        Returns: Optional[str]
        """
        return self._acceptance_statement
    
    @acceptance_statement.setter
    def acceptance_statement(self,value: Optional[str] = None) -> None:
        """
        Sets the acceptanceStatement property value. Administrator-supplied explanation of the terms and conditions, typically describing what it means to accept the terms and conditions set out in the T&C policy. This is shown to the user on prompts to accept the T&C policy.
        Args:
            value: Value to set for the acceptance_statement property.
        """
        self._acceptance_statement = value
    
    @property
    def acceptance_statuses(self,) -> Optional[List[terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus]]:
        """
        Gets the acceptanceStatuses property value. The list of acceptance statuses for this T&C policy.
        Returns: Optional[List[terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus]]
        """
        return self._acceptance_statuses
    
    @acceptance_statuses.setter
    def acceptance_statuses(self,value: Optional[List[terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus]] = None) -> None:
        """
        Sets the acceptanceStatuses property value. The list of acceptance statuses for this T&C policy.
        Args:
            value: Value to set for the acceptance_statuses property.
        """
        self._acceptance_statuses = value
    
    @property
    def assignments(self,) -> Optional[List[terms_and_conditions_assignment.TermsAndConditionsAssignment]]:
        """
        Gets the assignments property value. The list of assignments for this T&C policy.
        Returns: Optional[List[terms_and_conditions_assignment.TermsAndConditionsAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[terms_and_conditions_assignment.TermsAndConditionsAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for this T&C policy.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def body_text(self,) -> Optional[str]:
        """
        Gets the bodyText property value. Administrator-supplied body text of the terms and conditions, typically the terms themselves. This is shown to the user on prompts to accept the T&C policy.
        Returns: Optional[str]
        """
        return self._body_text
    
    @body_text.setter
    def body_text(self,value: Optional[str] = None) -> None:
        """
        Sets the bodyText property value. Administrator-supplied body text of the terms and conditions, typically the terms themselves. This is shown to the user on prompts to accept the T&C policy.
        Args:
            value: Value to set for the body_text property.
        """
        self._body_text = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermsAndConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TermsAndConditions()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Administrator-supplied description of the T&C policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Administrator-supplied description of the T&C policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Administrator-supplied name for the T&C policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Administrator-supplied name for the T&C policy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, terms_and_conditions_acceptance_status, terms_and_conditions_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptanceStatement": lambda n : setattr(self, 'acceptance_statement', n.get_str_value()),
            "acceptanceStatuses": lambda n : setattr(self, 'acceptance_statuses', n.get_collection_of_object_values(terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(terms_and_conditions_assignment.TermsAndConditionsAssignment)),
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
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Administrator-supplied title of the terms and conditions. This is shown to the user on prompts to accept the T&C policy.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Administrator-supplied title of the terms and conditions. This is shown to the user on prompts to accept the T&C policy.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Integer indicating the current version of the terms. Incremented when an administrator makes a change to the terms and wishes to require users to re-accept the modified T&C policy.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Integer indicating the current version of the terms. Incremented when an administrator makes a change to the terms and wishes to require users to re-accept the modified T&C policy.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

