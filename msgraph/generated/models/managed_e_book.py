from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_install_state, entity, e_book_install_summary, ios_vpp_e_book, managed_e_book_assignment, mime_content, user_install_state_summary

from . import entity

@dataclass
class ManagedEBook(entity.Entity):
    """
    An abstract class containing the base properties for Managed eBook.
    """
    # The list of assignments for this eBook.
    assignments: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]] = None
    # The date and time when the eBook file was created.
    created_date_time: Optional[datetime] = None
    # Description.
    description: Optional[str] = None
    # The list of installation states for this eBook.
    device_states: Optional[List[device_install_state.DeviceInstallState]] = None
    # Name of the eBook.
    display_name: Optional[str] = None
    # The more information Url.
    information_url: Optional[str] = None
    # Mobile App Install Summary.
    install_summary: Optional[e_book_install_summary.EBookInstallSummary] = None
    # Book cover.
    large_cover: Optional[mime_content.MimeContent] = None
    # The date and time when the eBook was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The privacy statement Url.
    privacy_information_url: Optional[str] = None
    # The date and time when the eBook was published.
    published_date_time: Optional[datetime] = None
    # Publisher.
    publisher: Optional[str] = None
    # The list of installation states for this eBook.
    user_state_summary: Optional[List[user_install_state_summary.UserInstallStateSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedEBook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedEBook
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBook".casefold():
            from . import ios_vpp_e_book

            return ios_vpp_e_book.IosVppEBook()
        return ManagedEBook()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_install_state, entity, e_book_install_summary, ios_vpp_e_book, managed_e_book_assignment, mime_content, user_install_state_summary

        from . import device_install_state, entity, e_book_install_summary, ios_vpp_e_book, managed_e_book_assignment, mime_content, user_install_state_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(managed_e_book_assignment.ManagedEBookAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(device_install_state.DeviceInstallState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationUrl": lambda n : setattr(self, 'information_url', n.get_str_value()),
            "installSummary": lambda n : setattr(self, 'install_summary', n.get_object_value(e_book_install_summary.EBookInstallSummary)),
            "largeCover": lambda n : setattr(self, 'large_cover', n.get_object_value(mime_content.MimeContent)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "privacyInformationUrl": lambda n : setattr(self, 'privacy_information_url', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "userStateSummary": lambda n : setattr(self, 'user_state_summary', n.get_collection_of_object_values(user_install_state_summary.UserInstallStateSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("informationUrl", self.information_url)
        writer.write_object_value("installSummary", self.install_summary)
        writer.write_object_value("largeCover", self.large_cover)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("privacyInformationUrl", self.privacy_information_url)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_str_value("publisher", self.publisher)
        writer.write_collection_of_object_values("userStateSummary", self.user_state_summary)
    

