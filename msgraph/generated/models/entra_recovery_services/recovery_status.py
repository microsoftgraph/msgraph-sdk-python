from enum import Enum

class RecoveryStatus(str, Enum):
    # Represents a job that has been initialized but has not been started yet
    Initialized = "initialized",
    # Represents a job that is in progress
    Running = "running",
    # Represents a job that ran successfully and is now complete
    Successful = "successful",
    # Represents a job that we were not able to run successfully
    Failed = "failed",
    # Represents a job that was abandoned by the user
    Abandoned = "abandoned",
    # This will help in making this enum evolable and adding more values in the future-
    UnknownFutureValue = "unknownFutureValue",
    # Represents a job for which we have started calculating the diff/preview.
    Calculating = "calculating",
    # Represents a job for which we have started loading data of the snapshot.
    LoadingData = "loadingData",

