from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mime_content = lazy_import('msgraph.generated.models.mime_content')
mobile_app_assignment = lazy_import('msgraph.generated.models.mobile_app_assignment')
mobile_app_category = lazy_import('msgraph.generated.models.mobile_app_category')
mobile_app_publishing_state = lazy_import('msgraph.generated.models.mobile_app_publishing_state')

class MobileApp(entity.Entity):
    """
    An abstract class containing the base properties for Intune mobile apps.
    """
    @property
    def assignments(self,) -> Optional[List[mobile_app_assignment.MobileAppAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for this mobile app.
        Returns: Optional[List[mobile_app_assignment.MobileAppAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[mobile_app_assignment.MobileAppAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for this mobile app.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def categories(self,) -> Optional[List[mobile_app_category.MobileAppCategory]]:
        """
        Gets the categories property value. The list of categories for this app.
        Returns: Optional[List[mobile_app_category.MobileAppCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[mobile_app_category.MobileAppCategory]] = None) -> None:
        """
        Sets the categories property value. The list of categories for this app.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mobileApp and sets the default values.
        """
        super().__init__()
        # The list of group assignments for this mobile app.
        self._assignments: Optional[List[mobile_app_assignment.MobileAppAssignment]] = None
        # The list of categories for this app.
        self._categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
        # The date and time the app was created.
        self._created_date_time: Optional[datetime] = None
        # The description of the app.
        self._description: Optional[str] = None
        # The developer of the app.
        self._developer: Optional[str] = None
        # The admin provided or imported title of the app.
        self._display_name: Optional[str] = None
        # The more information Url.
        self._information_url: Optional[str] = None
        # The value indicating whether the app is marked as featured by the admin.
        self._is_featured: Optional[bool] = None
        # The large icon, to be displayed in the app details and used for upload of the icon.
        self._large_icon: Optional[mime_content.MimeContent] = None
        # The date and time the app was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Notes for the app.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The owner of the app.
        self._owner: Optional[str] = None
        # The privacy statement Url.
        self._privacy_information_url: Optional[str] = None
        # The publisher of the app.
        self._publisher: Optional[str] = None
        # Indicates the publishing state of an app.
        self._publishing_state: Optional[mobile_app_publishing_state.MobileAppPublishingState] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the app was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the app was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileApp()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the app.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the app.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def developer(self,) -> Optional[str]:
        """
        Gets the developer property value. The developer of the app.
        Returns: Optional[str]
        """
        return self._developer
    
    @developer.setter
    def developer(self,value: Optional[str] = None) -> None:
        """
        Sets the developer property value. The developer of the app.
        Args:
            value: Value to set for the developer property.
        """
        self._developer = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The admin provided or imported title of the app.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The admin provided or imported title of the app.
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(mobile_app_assignment.MobileAppAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "developer": lambda n : setattr(self, 'developer', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "information_url": lambda n : setattr(self, 'information_url', n.get_str_value()),
            "is_featured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "large_icon": lambda n : setattr(self, 'large_icon', n.get_object_value(mime_content.MimeContent)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "privacy_information_url": lambda n : setattr(self, 'privacy_information_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "publishing_state": lambda n : setattr(self, 'publishing_state', n.get_enum_value(mobile_app_publishing_state.MobileAppPublishingState)),
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
    def is_featured(self,) -> Optional[bool]:
        """
        Gets the isFeatured property value. The value indicating whether the app is marked as featured by the admin.
        Returns: Optional[bool]
        """
        return self._is_featured
    
    @is_featured.setter
    def is_featured(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFeatured property value. The value indicating whether the app is marked as featured by the admin.
        Args:
            value: Value to set for the isFeatured property.
        """
        self._is_featured = value
    
    @property
    def large_icon(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the largeIcon property value. The large icon, to be displayed in the app details and used for upload of the icon.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._large_icon
    
    @large_icon.setter
    def large_icon(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the largeIcon property value. The large icon, to be displayed in the app details and used for upload of the icon.
        Args:
            value: Value to set for the largeIcon property.
        """
        self._large_icon = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the app was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the app was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes for the app.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes for the app.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The owner of the app.
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The owner of the app.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
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
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The publisher of the app.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The publisher of the app.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    @property
    def publishing_state(self,) -> Optional[mobile_app_publishing_state.MobileAppPublishingState]:
        """
        Gets the publishingState property value. Indicates the publishing state of an app.
        Returns: Optional[mobile_app_publishing_state.MobileAppPublishingState]
        """
        return self._publishing_state
    
    @publishing_state.setter
    def publishing_state(self,value: Optional[mobile_app_publishing_state.MobileAppPublishingState] = None) -> None:
        """
        Sets the publishingState property value. Indicates the publishing state of an app.
        Args:
            value: Value to set for the publishingState property.
        """
        self._publishing_state = value
    
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
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("developer", self.developer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("informationUrl", self.information_url)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_object_value("largeIcon", self.large_icon)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("privacyInformationUrl", self.privacy_information_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_enum_value("publishingState", self.publishing_state)
    

