from enum import Enum

class WhatIfAnalysisReasons(str, Enum):
    NotSet = "notSet",
    NotEnoughInformation = "notEnoughInformation",
    InvalidCondition = "invalidCondition",
    Users = "users",
    WorkloadIdentities = "workloadIdentities",
    Application = "application",
    UserActions = "userActions",
    AuthenticationContext = "authenticationContext",
    DevicePlatform = "devicePlatform",
    Devices = "devices",
    ClientApps = "clientApps",
    Location = "location",
    SignInRisk = "signInRisk",
    EmptyPolicy = "emptyPolicy",
    InvalidPolicy = "invalidPolicy",
    PolicyNotEnabled = "policyNotEnabled",
    UserRisk = "userRisk",
    Time = "time",
    InsiderRisk = "insiderRisk",
    AuthenticationFlow = "authenticationFlow",
    UnknownFutureValue = "unknownFutureValue",

