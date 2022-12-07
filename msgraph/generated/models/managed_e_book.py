from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_install_state = lazy_import('msgraph.generated.models.device_install_state')
e_book_install_summary = lazy_import('msgraph.generated.models.e_book_install_summary')
entity = lazy_import('msgraph.generated.models.entity')
managed_e_book_assignment = lazy_import('msgraph.generated.models.managed_e_book_assignment')
mime_content = lazy_import('msgraph.generated.models.mime_content')
user_install_state_summary = lazy_import('msgraph.generated.models.user_install_state_summary')

class ManagedEBook(entity.Entity):
    """
    An abstract class containing the base properties for Managed eBook.
    """
    @property
    def assignments(self,) -> Optional[List[managed_e_book_assignment.ManagedEBookAssignment]]:
        """
        Gets the assignments property value. The list of assignments for this eBook.
        Returns: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for this eBook.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedEBook and sets the default values.
        """
        super().__init__()
        # The list of assignments for this eBook.
        self._assignments: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]] = None
        # The date and time when the eBook file was created.
        self._created_date_time: Optional[datetime] = None
        # Description.
        self._description: Optional[str] = None
        # The list of installation states for this eBook.
        self._device_states: Optional[List[device_install_state.DeviceInstallState]] = None
        # Name of the eBook.
        self._display_name: Optional[str] = None
        # The more information Url.
        self._information_url: Optional[str] = None
        # Mobile App Install Summary.
        self._install_summary: Optional[e_book_install_summary.EBookInstallSummary] = None
        # Book cover.
        self._large_cover: Optional[mime_content.MimeContent] = None
        # The date and time when the eBook was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The privacy statement Url.
        self._privacy_information_url: Optional[str] = None
        # The date and time when the eBook was published.
        self._published_date_time: Optional[datetime] = None
        # Publisher.
        self._publisher: Optional[str] = None
        # The list of installation states for this eBook.
        self._user_state_summary: Optional[List[user_install_state_summary.UserInstallStateSummary]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the eBook file was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the eBook file was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedEBook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedEBook
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedEBook()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_states(self,) -> Optional[List[device_install_state.DeviceInstallState]]:
        """
        Gets the deviceStates property value. The list of installation states for this eBook.
        Returns: Optional[List[device_install_state.DeviceInstallState]]
        """
        return self._device_states
    
    @device_states.setter
    def device_states(self,value: Optional[List[device_install_state.DeviceInstallState]] = None) -> None:
        """
        Sets the deviceStates property value. The list of installation states for this eBook.
        Args:
            value: Value to set for the deviceStates property.
        """
        self._device_states = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the eBook.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the eBook.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(managed_e_book_assignment.ManagedEBookAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_states": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(device_install_state.DeviceInstallState)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "information_url": lambda n : setattr(self, 'information_url', n.get_str_value()),
            "install_summary": lambda n : setattr(self, 'install_summary', n.get_object_value(e_book_install_summary.EBookInstallSummary)),
            "large_cover": lambda n : setattr(self, 'large_cover', n.get_object_value(mime_content.MimeContent)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "privacy_information_url": lambda n : setattr(self, 'privacy_information_url', n.get_str_value()),
            "published_date_time": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "user_state_summary": lambda n : setattr(self, 'user_state_summary', n.get_collection_of_object_values(user_install_state_summary.UserInstallStateSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def information_url(self,) -> Optional[str]:
        """
        Gets the informationUrl property value. The more information Url.
        Returns: Optional[str]
        """
        return self._information_url
    
    @information_url.setter
    def information_url(self,value: Optional[str] = None) -> None:
        """
        Sets the informationUrl property value. The more information Url.
        Args:
            value: Value to set for the informationUrl property.
        """
        self._information_url = value
    
    @property
    def install_summary(self,) -> Optional[e_book_install_summary.EBookInstallSummary]:
        """
        Gets the installSummary property value. Mobile App Install Summary.
        Returns: Optional[e_book_install_summary.EBookInstallSummary]
        """
        return self._install_summary
    
    @install_summary.setter
    def install_summary(self,value: Optional[e_book_install_summary.EBookInstallSummary] = None) -> None:
        """
        Sets the installSummary property value. Mobile App Install Summary.
        Args:
            value: Value to set for the installSummary property.
        """
        self._install_summary = value
    
    @property
    def large_cover(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the largeCover property value. Book cover.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._large_cover
    
    @large_cover.setter
    def large_cover(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the largeCover property value. Book cover.
        Args:
            value: Value to set for the largeCover property.
        """
        self._large_cover = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the eBook was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the eBook was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def privacy_information_url(self,) -> Optional[str]:
        """
        Gets the privacyInformationUrl property value. The privacy statement Url.
        Returns: Optional[str]
        """
        return self._privacy_information_url
    
    @privacy_information_url.setter
    def privacy_information_url(self,value: Optional[str] = None) -> None:
        """
        Sets the privacyInformationUrl property value. The privacy statement Url.
        Args:
            value: Value to set for the privacyInformationUrl property.
        """
        self._privacy_information_url = value
    
    @property
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. The date and time when the eBook was published.
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. The date and time when the eBook was published.
        Args:
            value: Value to set for the publishedDateTime property.
        """
        self._published_date_time = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. Publisher.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. Publisher.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def user_state_summary(self,) -> Optional[List[user_install_state_summary.UserInstallStateSummary]]:
        """
        Gets the userStateSummary property value. The list of installation states for this eBook.
        Returns: Optional[List[user_install_state_summary.UserInstallStateSummary]]
        """
        return self._user_state_summary
    
    @user_state_summary.setter
    def user_state_summary(self,value: Optional[List[user_install_state_summary.UserInstallStateSummary]] = None) -> None:
        """
        Sets the userStateSummary property value. The list of installation states for this eBook.
        Args:
            value: Value to set for the userStateSummary property.
        """
        self._user_state_summary = value
    

