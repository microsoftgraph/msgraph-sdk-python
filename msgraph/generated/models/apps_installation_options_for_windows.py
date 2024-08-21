from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AppsInstallationOptionsForWindows(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies whether users can install Microsoft 365 apps, including Skype for Business, on their Windows devices. The default value is true.
    is_microsoft365_apps_enabled: Optional[bool] = None
    # Specifies whether users can install Microsoft Project on their Windows devices. The default value is true.
    is_project_enabled: Optional[bool] = None
    # Specifies whether users can install Skype for Business (standalone) on their Windows devices. The default value is true.
    is_skype_for_business_enabled: Optional[bool] = None
    # Specifies whether users can install Visio on their Windows devices. The default value is true.
    is_visio_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppsInstallationOptionsForWindows:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppsInstallationOptionsForWindows
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppsInstallationOptionsForWindows()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isMicrosoft365AppsEnabled": lambda n : setattr(self, 'is_microsoft365_apps_enabled', n.get_bool_value()),
            "isProjectEnabled": lambda n : setattr(self, 'is_project_enabled', n.get_bool_value()),
            "isSkypeForBusinessEnabled": lambda n : setattr(self, 'is_skype_for_business_enabled', n.get_bool_value()),
            "isVisioEnabled": lambda n : setattr(self, 'is_visio_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isMicrosoft365AppsEnabled", self.is_microsoft365_apps_enabled)
        writer.write_bool_value("isProjectEnabled", self.is_project_enabled)
        writer.write_bool_value("isSkypeForBusinessEnabled", self.is_skype_for_business_enabled)
        writer.write_bool_value("isVisioEnabled", self.is_visio_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

