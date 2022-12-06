from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
notebook_links = lazy_import('msgraph.generated.models.notebook_links')
onenote_user_role = lazy_import('msgraph.generated.models.onenote_user_role')

class CopyNotebookModel(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CopyNotebookModel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The createdBy property
        self._created_by: Optional[str] = None
        # The createdByIdentity property
        self._created_by_identity: Optional[identity_set.IdentitySet] = None
        # The createdTime property
        self._created_time: Optional[datetime] = None
        # The id property
        self._id: Optional[str] = None
        # The isDefault property
        self._is_default: Optional[bool] = None
        # The isShared property
        self._is_shared: Optional[bool] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[str] = None
        # The lastModifiedByIdentity property
        self._last_modified_by_identity: Optional[identity_set.IdentitySet] = None
        # The lastModifiedTime property
        self._last_modified_time: Optional[datetime] = None
        # The links property
        self._links: Optional[notebook_links.NotebookLinks] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The sectionGroupsUrl property
        self._section_groups_url: Optional[str] = None
        # The sectionsUrl property
        self._sections_url: Optional[str] = None
        # The self property
        self._self: Optional[str] = None
        # The userRole property
        self._user_role: Optional[onenote_user_role.OnenoteUserRole] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_by_identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdByIdentity property value. The createdByIdentity property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by_identity
    
    @created_by_identity.setter
    def created_by_identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdByIdentity property value. The createdByIdentity property
        Args:
            value: Value to set for the createdByIdentity property.
        """
        self._created_by_identity = value
    
    @property
    def created_time(self,) -> Optional[datetime]:
        """
        Gets the createdTime property value. The createdTime property
        Returns: Optional[datetime]
        """
        return self._created_time
    
    @created_time.setter
    def created_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdTime property value. The createdTime property
        Args:
            value: Value to set for the createdTime property.
        """
        self._created_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyNotebookModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CopyNotebookModel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CopyNotebookModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_by_identity": lambda n : setattr(self, 'created_by_identity', n.get_object_value(identity_set.IdentitySet)),
            "created_time": lambda n : setattr(self, 'created_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_shared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "last_modified_by_identity": lambda n : setattr(self, 'last_modified_by_identity', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_time": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(notebook_links.NotebookLinks)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "section_groups_url": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections_url": lambda n : setattr(self, 'sections_url', n.get_str_value()),
            "self": lambda n : setattr(self, 'self', n.get_str_value()),
            "user_role": lambda n : setattr(self, 'user_role', n.get_enum_value(onenote_user_role.OnenoteUserRole)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. The isDefault property
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. The isDefault property
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_shared(self,) -> Optional[bool]:
        """
        Gets the isShared property value. The isShared property
        Returns: Optional[bool]
        """
        return self._is_shared
    
    @is_shared.setter
    def is_shared(self,value: Optional[bool] = None) -> None:
        """
        Sets the isShared property value. The isShared property
        Args:
            value: Value to set for the isShared property.
        """
        self._is_shared = value
    
    @property
    def last_modified_by(self,) -> Optional[str]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[str]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_by_identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedByIdentity property value. The lastModifiedByIdentity property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by_identity
    
    @last_modified_by_identity.setter
    def last_modified_by_identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedByIdentity property value. The lastModifiedByIdentity property
        Args:
            value: Value to set for the lastModifiedByIdentity property.
        """
        self._last_modified_by_identity = value
    
    @property
    def last_modified_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedTime property value. The lastModifiedTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_time
    
    @last_modified_time.setter
    def last_modified_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedTime property value. The lastModifiedTime property
        Args:
            value: Value to set for the lastModifiedTime property.
        """
        self._last_modified_time = value
    
    @property
    def links(self,) -> Optional[notebook_links.NotebookLinks]:
        """
        Gets the links property value. The links property
        Returns: Optional[notebook_links.NotebookLinks]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[notebook_links.NotebookLinks] = None) -> None:
        """
        Sets the links property value. The links property
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def section_groups_url(self,) -> Optional[str]:
        """
        Gets the sectionGroupsUrl property value. The sectionGroupsUrl property
        Returns: Optional[str]
        """
        return self._section_groups_url
    
    @section_groups_url.setter
    def section_groups_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionGroupsUrl property value. The sectionGroupsUrl property
        Args:
            value: Value to set for the sectionGroupsUrl property.
        """
        self._section_groups_url = value
    
    @property
    def sections_url(self,) -> Optional[str]:
        """
        Gets the sectionsUrl property value. The sectionsUrl property
        Returns: Optional[str]
        """
        return self._sections_url
    
    @sections_url.setter
    def sections_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionsUrl property value. The sectionsUrl property
        Args:
            value: Value to set for the sectionsUrl property.
        """
        self._sections_url = value
    
    @property
    def self(self,) -> Optional[str]:
        """
        Gets the self property value. The self property
        Returns: Optional[str]
        """
        return self._self
    
    @self.setter
    def self(self,value: Optional[str] = None) -> None:
        """
        Sets the self property value. The self property
        Args:
            value: Value to set for the self property.
        """
        self._self = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("createdBy", self.created_by)
        writer.write_object_value("createdByIdentity", self.created_by_identity)
        writer.write_datetime_value("createdTime", self.created_time)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("lastModifiedByIdentity", self.last_modified_by_identity)
        writer.write_datetime_value("lastModifiedTime", self.last_modified_time)
        writer.write_object_value("links", self.links)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sectionGroupsUrl", self.section_groups_url)
        writer.write_str_value("sectionsUrl", self.sections_url)
        writer.write_str_value("self", self.self)
        writer.write_enum_value("userRole", self.user_role)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_role(self,) -> Optional[onenote_user_role.OnenoteUserRole]:
        """
        Gets the userRole property value. The userRole property
        Returns: Optional[onenote_user_role.OnenoteUserRole]
        """
        return self._user_role
    
    @user_role.setter
    def user_role(self,value: Optional[onenote_user_role.OnenoteUserRole] = None) -> None:
        """
        Sets the userRole property value. The userRole property
        Args:
            value: Value to set for the userRole property.
        """
        self._user_role = value
    

