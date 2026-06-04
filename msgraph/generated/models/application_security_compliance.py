from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .csa_star_level import CsaStarLevel
    from .fed_ramp_level import FedRampLevel
    from .pci_version import PciVersion

@dataclass
class ApplicationSecurityCompliance(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the application adheres to the Control Objectives for Information and Related Technologies (COBIT) framework.
    cobit: Optional[bool] = None
    # Indicates whether the application complies with the Children’s Online Privacy Protection Act (COPPA).
    coppa: Optional[bool] = None
    # Specifies the Cloud Security Alliance (CSA) Security, Trust & Assurance Registry (STAR) certification level. The possible values are: none, attestation, certification, continuousMonitoring, cStarAssessment, selfAssessment, notSupported, unknownFutureValue.
    csa_star: Optional[CsaStarLevel] = None
    # Specifies the Federal Risk and Authorization Management Program (FedRAMP) certification level. The possible values are: none, high, liSaas, low, moderate, notSupported, unknownFutureValue.
    fed_ramp: Optional[FedRampLevel] = None
    # Indicates whether the application complies with the Family Educational Rights and Privacy Act (FERPA).
    ferpa: Optional[bool] = None
    # Indicates whether the application meets Federal Financial Institutions Examination Council (FFIEC) requirements.
    ffiec: Optional[bool] = None
    # Indicates whether the application complies with Financial Industry Regulatory Authority (FINRA) standards.
    finra: Optional[bool] = None
    # Indicates whether the application complies with the Federal Information Security Management Act (FISMA).
    fisma: Optional[bool] = None
    # Indicates whether the application provider adheres to Generally Accepted Accounting Principles (GAAP).
    gaap: Optional[bool] = None
    # Indicates whether the application adheres to Generally Accepted Privacy Principles (GAPP).
    gapp: Optional[bool] = None
    # Indicates whether the application complies with the Gramm–Leach–Bliley Act (GLBA) for financial data protection.
    glba: Optional[bool] = None
    # Indicates whether the application complies with the Health Insurance Portability and Accountability Act (HIPAA).
    hipaa: Optional[bool] = None
    # Indicates whether the application holds HITRUST certification, demonstrating alignment with healthcare and data security standards.
    hitrust: Optional[bool] = None
    # Indicates whether the application complies with International Standard on Assurance Engagements (ISAE) 3402 requirements.
    isae3402: Optional[bool] = None
    # Indicates whether the application is certified against ISO/IEC 27001 for information security management systems (ISMS).
    iso27001: Optional[bool] = None
    # Indicates whether the application follows ISO/IEC 27002 security control best practices.
    iso27002: Optional[bool] = None
    # Indicates whether the application complies with ISO/IEC 27017 standards for cloud security controls.
    iso27017: Optional[bool] = None
    # Indicates whether the application complies with ISO/IEC 27018 standards for protecting personally identifiable information (PII) in cloud environments.
    iso27018: Optional[bool] = None
    # Indicates whether the application complies with International Traffic in Arms Regulations (ITAR).
    itar: Optional[bool] = None
    # Indicates whether the application aligns with Jericho Forum security principles for deperimeterized environments.
    jericho_forum_commandments: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the Payment Card Industry (PCI) Data Security Standard (DSS) version the application complies with. The possible values are: none, v321, v4, notSupported, unknownFutureValue.
    pci: Optional[PciVersion] = None
    # Indicates whether the application complies with the EU–U.S. Privacy Shield framework for cross-border data transfers.
    privacy_shield: Optional[bool] = None
    # Indicates whether the application previously adhered to the U.S.–EU Safe Harbor data transfer framework.
    safe_harbor: Optional[bool] = None
    # Indicates whether the application provider undergoes a Service Organization Control (SOC) one audit report.
    soc1: Optional[bool] = None
    # Indicates whether the application provider undergoes a Service Organization Control (SOC) two audit report.
    soc2: Optional[bool] = None
    # Indicates whether the application provider undergoes a Service Organization Control (SOC) three audit report.
    soc3: Optional[bool] = None
    # Indicates whether the application complies with the Sarbanes–Oxley Act (SOX) financial reporting requirements.
    sox: Optional[bool] = None
    # Indicates whether the application aligns with National Institute of Standards and Technology (NIST) Special Publication 800-53 security and privacy controls.
    sp800_53: Optional[bool] = None
    # Indicates whether the application adheres to Statement on Standards for Attestation Engagements (SSAE) No. 16.
    ssae16: Optional[bool] = None
    # Indicates whether the application complies with U.S. Trade Representative (USTR) data and trade protection requirements.
    ustr: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationSecurityCompliance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSecurityCompliance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationSecurityCompliance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .csa_star_level import CsaStarLevel
        from .fed_ramp_level import FedRampLevel
        from .pci_version import PciVersion

        from .csa_star_level import CsaStarLevel
        from .fed_ramp_level import FedRampLevel
        from .pci_version import PciVersion

        fields: dict[str, Callable[[Any], None]] = {
            "cobit": lambda n : setattr(self, 'cobit', n.get_bool_value()),
            "coppa": lambda n : setattr(self, 'coppa', n.get_bool_value()),
            "csaStar": lambda n : setattr(self, 'csa_star', n.get_enum_value(CsaStarLevel)),
            "fedRamp": lambda n : setattr(self, 'fed_ramp', n.get_enum_value(FedRampLevel)),
            "ferpa": lambda n : setattr(self, 'ferpa', n.get_bool_value()),
            "ffiec": lambda n : setattr(self, 'ffiec', n.get_bool_value()),
            "finra": lambda n : setattr(self, 'finra', n.get_bool_value()),
            "fisma": lambda n : setattr(self, 'fisma', n.get_bool_value()),
            "gaap": lambda n : setattr(self, 'gaap', n.get_bool_value()),
            "gapp": lambda n : setattr(self, 'gapp', n.get_bool_value()),
            "glba": lambda n : setattr(self, 'glba', n.get_bool_value()),
            "hipaa": lambda n : setattr(self, 'hipaa', n.get_bool_value()),
            "hitrust": lambda n : setattr(self, 'hitrust', n.get_bool_value()),
            "isae3402": lambda n : setattr(self, 'isae3402', n.get_bool_value()),
            "iso27001": lambda n : setattr(self, 'iso27001', n.get_bool_value()),
            "iso27002": lambda n : setattr(self, 'iso27002', n.get_bool_value()),
            "iso27017": lambda n : setattr(self, 'iso27017', n.get_bool_value()),
            "iso27018": lambda n : setattr(self, 'iso27018', n.get_bool_value()),
            "itar": lambda n : setattr(self, 'itar', n.get_bool_value()),
            "jerichoForumCommandments": lambda n : setattr(self, 'jericho_forum_commandments', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pci": lambda n : setattr(self, 'pci', n.get_enum_value(PciVersion)),
            "privacyShield": lambda n : setattr(self, 'privacy_shield', n.get_bool_value()),
            "safeHarbor": lambda n : setattr(self, 'safe_harbor', n.get_bool_value()),
            "soc1": lambda n : setattr(self, 'soc1', n.get_bool_value()),
            "soc2": lambda n : setattr(self, 'soc2', n.get_bool_value()),
            "soc3": lambda n : setattr(self, 'soc3', n.get_bool_value()),
            "sox": lambda n : setattr(self, 'sox', n.get_bool_value()),
            "sp800_53": lambda n : setattr(self, 'sp800_53', n.get_bool_value()),
            "ssae16": lambda n : setattr(self, 'ssae16', n.get_bool_value()),
            "ustr": lambda n : setattr(self, 'ustr', n.get_bool_value()),
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
        writer.write_bool_value("cobit", self.cobit)
        writer.write_bool_value("coppa", self.coppa)
        writer.write_enum_value("csaStar", self.csa_star)
        writer.write_enum_value("fedRamp", self.fed_ramp)
        writer.write_bool_value("ferpa", self.ferpa)
        writer.write_bool_value("ffiec", self.ffiec)
        writer.write_bool_value("finra", self.finra)
        writer.write_bool_value("fisma", self.fisma)
        writer.write_bool_value("gaap", self.gaap)
        writer.write_bool_value("gapp", self.gapp)
        writer.write_bool_value("glba", self.glba)
        writer.write_bool_value("hipaa", self.hipaa)
        writer.write_bool_value("hitrust", self.hitrust)
        writer.write_bool_value("isae3402", self.isae3402)
        writer.write_bool_value("iso27001", self.iso27001)
        writer.write_bool_value("iso27002", self.iso27002)
        writer.write_bool_value("iso27017", self.iso27017)
        writer.write_bool_value("iso27018", self.iso27018)
        writer.write_bool_value("itar", self.itar)
        writer.write_bool_value("jerichoForumCommandments", self.jericho_forum_commandments)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("pci", self.pci)
        writer.write_bool_value("privacyShield", self.privacy_shield)
        writer.write_bool_value("safeHarbor", self.safe_harbor)
        writer.write_bool_value("soc1", self.soc1)
        writer.write_bool_value("soc2", self.soc2)
        writer.write_bool_value("soc3", self.soc3)
        writer.write_bool_value("sox", self.sox)
        writer.write_bool_value("sp800_53", self.sp800_53)
        writer.write_bool_value("ssae16", self.ssae16)
        writer.write_bool_value("ustr", self.ustr)
        writer.write_additional_data_value(self.additional_data)
    

