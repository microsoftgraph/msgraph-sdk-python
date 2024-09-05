# Changelog

All notable changes to this project will be documented in this file.


## [1.6.0](https://github.com/microsoftgraph/msgraph-sdk-python/compare/v1.5.4...v1.6.0) (2024-09-05)


### Features

* readme formatting to trigger release please ([0e45705](https://github.com/microsoftgraph/msgraph-sdk-python/commit/0e457051f4fa522cbff81c5359f0ff6a8fcdece4))

## [1.5.4](https://github.com/microsoftgraph/msgraph-sdk-python/compare/v1.5.3...v1.5.4) (2024-08-02)


### Bug Fixes

* requires a higher version of the JSON dependency ([955f85f](https://github.com/microsoftgraph/msgraph-sdk-python/commit/955f85fe35ddfc0eb6f2f2c6a58d59ec04f3b073))

## [1.5.3](https://github.com/microsoftgraph/msgraph-sdk-python/compare/v1.5.2...v1.5.3) (2024-07-17)


### Bug Fixes

* higher kiota abstractions requirement to avoid missing multipart ([d6c9f86](https://github.com/microsoftgraph/msgraph-sdk-python/commit/d6c9f860420065092fdf33ea03518236b0286358))

## [1.5.2](https://github.com/microsoftgraph/msgraph-sdk-python/compare/v1.5.1...v1.5.2) (2024-07-10)


### Bug Fixes

* fixes module name for release ([941f6b2](https://github.com/microsoftgraph/msgraph-sdk-python/commit/941f6b2325555962af9c412c05b609797d7319c4))

## [1.5.1](https://github.com/microsoftgraph/msgraph-sdk-python/compare/v1.5.0...v1.5.1) (2024-07-09)


### Bug Fixes

* avoid using default mutable arguments ([4912f5a](https://github.com/microsoftgraph/msgraph-sdk-python/commit/4912f5a54c9063a42b3edf9f1276878d49e5bf6b))


### Documentation

* fix typo in README ([71463a6](https://github.com/microsoftgraph/msgraph-sdk-python/commit/71463a64fa3c3e43cb5f4c36f46a1aef3a703b29))

## [1.5.0] - 2024-05-23

### Changed

- Weekly generation with Kiota - 21st May 2024

## [1.4.0] - 2024-05-08

### Changed

- Weekly generation with Kiota - 7th May 2024
- Updated Request Configuration set up, allowing for default request Configuration
as well as the Request builder custom Requestconfiguration for backward compatibility.

## [1.3.0] - 2024-04-16

### Changed

- Weekly generation with Kiota.

## [1.2.0] - 2024-03-19

### Added

- Added support for form and multipart serialization.

### Changed
 - Latest metadata updates from 24th March 2024.

## [1.1.0] - 2024-01-24

### Added

### Changed
 - Latest metadata updates from 23rd January 2024.

## [1.0.0] - 2023-10-31

### Added

### Changed
 - GA Release.

## [1.0.0rc1] - 2023-10-30

### Added

### Changed
 - Fixed a bug where some model properties were in camelcase instead of snakecase.

## [1.0.0rc0] - 2023-10-27

### Added

### Changed
 - Refactored request headers from dictionary to headercollection.

## [1.0.0a16] - 2023-09-19

### Added

### Changed
 - Fix issue with using raw url in request builder due to incorrect parameter order.

## [1.0.0a15] - 2023-09-13

### Added

- Added request translation method to native request object
- Added opentelemetry to support observability.
- Added support for continous access evaluation.

### Changed
 - Switched from uritemplate to std-uritemplate for URI templating.

## [1.0.0a14] - 2023-08-09

### Added

- Added backing store support and enabled backing store by default.

### Changed

## [1.0.0a13] - 2023-05-25

### Added

### Changed

- Simplified the creation of a graph client. [#180](https://github.com/microsoftgraph/msgraph-sdk-python/issues/180)

## [1.0.0a12] - 2023-04-19

### Added

### Changed

- Changed the request builders api to include indexers as part of the path. [#2528](https://github.com/microsoft/kiota/issues/2528)

## [1.0.0a11] - 2023-04-05

### Added

### Changed

- Fixed a bug where UUIDs were being passed as u_u_i_d to desrialization methods.

## [1.0.0a10] - 2023-03-28

### Added

### Changed

- Refactored the import mechanism to use conditional and deferred imports.
- Fixed a bug where discriminator methods were missing some valid types.
- Fixed a bug where the date and guid types were improperly mapped.
- Re-ordered method hierarchy to match python conventions

## [1.0.0a9] - 2023-01-25

### Added

### Changed

- Fixed bug with classes with namespace being generated outside of the namespace [#55](https://github.com/microsoftgraph/msgraph-sdk-python/issues/55)
