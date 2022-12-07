from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_approval_stage = lazy_import('msgraph.generated.models.access_package_approval_stage')

class AccessPackageAssignmentApprovalSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new accessPackageAssignmentApprovalSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If false, then approval is not required for new requests in this policy.
        self._is_approval_required_for_add: Optional[bool] = None
        # If false, then approval is not required for updates to requests in this policy.
        self._is_approval_required_for_update: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If approval is required, the one, two or three elements of this collection define each of the stages of approval. An empty array is present if no approval is required.
        self._stages: Optional[List[access_package_approval_stage.AccessPackageApprovalStage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentApprovalSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentApprovalSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentApprovalSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_approval_required_for_add": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "is_approval_required_for_update": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(access_package_approval_stage.AccessPackageApprovalStage)),
        }
        return fields
    
    @property
    def is_approval_required_for_add(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForAdd property value. If false, then approval is not required for new requests in this policy.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_add
    
    @is_approval_required_for_add.setter
    def is_approval_required_for_add(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForAdd property value. If false, then approval is not required for new requests in this policy.
        Args:
            value: Value to set for the isApprovalRequiredForAdd property.
        """
        self._is_approval_required_for_add = value
    
    @property
    def is_approval_required_for_update(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForUpdate property value. If false, then approval is not required for updates to requests in this policy.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_update
    
    @is_approval_required_for_update.setter
    def is_approval_required_for_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForUpdate property value. If false, then approval is not required for updates to requests in this policy.
        Args:
            value: Value to set for the isApprovalRequiredForUpdate property.
        """
        self._is_approval_required_for_update = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stages(self,) -> Optional[List[access_package_approval_stage.AccessPackageApprovalStage]]:
        """
        Gets the stages property value. If approval is required, the one, two or three elements of this collection define each of the stages of approval. An empty array is present if no approval is required.
        Returns: Optional[List[access_package_approval_stage.AccessPackageApprovalStage]]
        """
        return self._stages
    
    @stages.setter
    def stages(self,value: Optional[List[access_package_approval_stage.AccessPackageApprovalStage]] = None) -> None:
        """
        Sets the stages property value. If approval is required, the one, two or three elements of this collection define each of the stages of approval. An empty array is present if no approval is required.
        Args:
            value: Value to set for the stages property.
        """
        self._stages = value
    

