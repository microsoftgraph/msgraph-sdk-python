from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_class import EducationClass
    from .education_school import EducationSchool
    from .education_user import EducationUser
    from .reports_root import ReportsRoot

@dataclass
class EducationRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The classes property
    classes: Optional[list[EducationClass]] = None
    # The me property
    me: Optional[EducationUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reports property
    reports: Optional[ReportsRoot] = None
    # The schools property
    schools: Optional[list[EducationSchool]] = None
    # The users property
    users: Optional[list[EducationUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_class import EducationClass
        from .education_school import EducationSchool
        from .education_user import EducationUser
        from .reports_root import ReportsRoot

        from .education_class import EducationClass
        from .education_school import EducationSchool
        from .education_user import EducationUser
        from .reports_root import ReportsRoot

        fields: dict[str, Callable[[Any], None]] = {
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(EducationClass)),
            "me": lambda n : setattr(self, 'me', n.get_object_value(EducationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(ReportsRoot)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(EducationSchool)),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(EducationUser)),
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
        writer.write_collection_of_object_values("classes", self.classes)
        writer.write_object_value("me", self.me)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("schools", self.schools)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

