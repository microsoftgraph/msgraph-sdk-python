from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_risk_factor_legal_info_gdpr import ApplicationRiskFactorLegalInfoGdpr
    from .data_retention_level import DataRetentionLevel

@dataclass
class ApplicationRiskFactorLegalInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The dataRetention property
    data_retention: Optional[DataRetentionLevel] = None
    # The gdpr property
    gdpr: Optional[ApplicationRiskFactorLegalInfoGdpr] = None
    # Indicates whether customers maintain ownership and control of their data processed or stored by the application.
    has_data_ownership: Optional[bool] = None
    # Indicates whether the application or organization complies with the Digital Millennium Copyright Act (DMCA) or equivalent copyright protection frameworks.
    has_dmca: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactorLegalInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactorLegalInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactorLegalInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_risk_factor_legal_info_gdpr import ApplicationRiskFactorLegalInfoGdpr
        from .data_retention_level import DataRetentionLevel

        from .application_risk_factor_legal_info_gdpr import ApplicationRiskFactorLegalInfoGdpr
        from .data_retention_level import DataRetentionLevel

        fields: dict[str, Callable[[Any], None]] = {
            "dataRetention": lambda n : setattr(self, 'data_retention', n.get_enum_value(DataRetentionLevel)),
            "gdpr": lambda n : setattr(self, 'gdpr', n.get_object_value(ApplicationRiskFactorLegalInfoGdpr)),
            "hasDataOwnership": lambda n : setattr(self, 'has_data_ownership', n.get_bool_value()),
            "hasDmca": lambda n : setattr(self, 'has_dmca', n.get_bool_value()),
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
        writer.write_enum_value("dataRetention", self.data_retention)
        writer.write_object_value("gdpr", self.gdpr)
        writer.write_bool_value("hasDataOwnership", self.has_data_ownership)
        writer.write_bool_value("hasDmca", self.has_dmca)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

