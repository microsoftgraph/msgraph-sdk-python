from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WipePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The keepEnrollmentData property
    keep_enrollment_data: Optional[bool] = None
    # The keepUserData property
    keep_user_data: Optional[bool] = None
    # The macOsUnlockCode property
    mac_os_unlock_code: Optional[str] = None
    # The persistEsimDataPlan property
    persist_esim_data_plan: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WipePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WipePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WipePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "keepEnrollmentData": lambda n : setattr(self, 'keep_enrollment_data', n.get_bool_value()),
            "keepUserData": lambda n : setattr(self, 'keep_user_data', n.get_bool_value()),
            "macOsUnlockCode": lambda n : setattr(self, 'mac_os_unlock_code', n.get_str_value()),
            "persistEsimDataPlan": lambda n : setattr(self, 'persist_esim_data_plan', n.get_bool_value()),
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
        writer.write_bool_value("keepEnrollmentData", self.keep_enrollment_data)
        writer.write_bool_value("keepUserData", self.keep_user_data)
        writer.write_str_value("macOsUnlockCode", self.mac_os_unlock_code)
        writer.write_bool_value("persistEsimDataPlan", self.persist_esim_data_plan)
        writer.write_additional_data_value(self.additional_data)
    

