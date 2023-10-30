# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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