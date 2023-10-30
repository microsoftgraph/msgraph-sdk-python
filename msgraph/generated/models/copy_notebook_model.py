from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .notebook_links import NotebookLinks
    from .onenote_user_role import OnenoteUserRole

@dataclass
class CopyNotebookModel(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The createdBy property
    created_by: Optional[str] = None
    # The createdByIdentity property
    created_by_identity: Optional[IdentitySet] = None
    # The createdTime property
    created_time: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The isDefault property
    is_default: Optional[bool] = None
    # The isShared property
    is_shared: Optional[bool] = None
    # The lastModifiedBy property
    last_modified_by: Optional[str] = None
    # The lastModifiedByIdentity property
    last_modified_by_identity: Optional[IdentitySet] = None
    # The lastModifiedTime property
    last_modified_time: Optional[datetime.datetime] = None
    # The links property
    links: Optional[NotebookLinks] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sectionGroupsUrl property
    section_groups_url: Optional[str] = None
    # The sectionsUrl property
    sections_url: Optional[str] = None
    # The self property
    self: Optional[str] = None
    # The userRole property
    user_role: Optional[OnenoteUserRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyNotebookModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopyNotebookModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CopyNotebookModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .notebook_links import NotebookLinks
        from .onenote_user_role import OnenoteUserRole

        from .identity_set import IdentitySet
        from .notebook_links import NotebookLinks
        from .onenote_user_role import OnenoteUserRole

        fields: Dict[str, Callable[[Any], None]] = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_by_identity": lambda n : setattr(self, 'created_by_identity', n.get_object_value(IdentitySet)),
            "created_time": lambda n : setattr(self, 'created_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_shared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "last_modified_by_identity": lambda n : setattr(self, 'last_modified_by_identity', n.get_object_value(IdentitySet)),
            "last_modified_time": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(NotebookLinks)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "section_groups_url": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections_url": lambda n : setattr(self, 'sections_url', n.get_str_value()),
            "self": lambda n : setattr(self, 'self', n.get_str_value()),
            "user_role": lambda n : setattr(self, 'user_role', n.get_enum_value(OnenoteUserRole)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("created_by", self.created_by)
        writer.write_object_value("created_by_identity", self.created_by_identity)
        writer.write_datetime_value("created_time", self.created_time)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("is_default", self.is_default)
        writer.write_bool_value("is_shared", self.is_shared)
        writer.write_str_value("last_modified_by", self.last_modified_by)
        writer.write_object_value("last_modified_by_identity", self.last_modified_by_identity)
        writer.write_datetime_value("last_modified_time", self.last_modified_time)
        writer.write_object_value("links", self.links)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("section_groups_url", self.section_groups_url)
        writer.write_str_value("sections_url", self.sections_url)
        writer.write_str_value("self", self.self)
        writer.write_enum_value("user_role", self.user_role)
        writer.write_additional_data_value(self.additional_data)
    

