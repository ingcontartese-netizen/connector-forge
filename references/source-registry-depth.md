# Source Registry Depth

Use this when the first surface scan looks thin or says there is no API.

## Problem

Desktop and enterprise apps often expose control through local SDKs, integration APIs, CLIs, plugins, import/export formats, installed examples, or embedded libraries. Stopping at "no REST port" is too shallow.

## Rule

Before declaring a programmable surface absent, check:

- official docs and release notes;
- SDK/API reference, including "Professional", "Integration", or local-mode APIs;
- installed JAR/DLL/shared libraries;
- demo apps and sample databases;
- CLI tools and command-line switches;
- plugin/add-on APIs;
- file workflows: XML, XER, Excel, CSV, reports;
- local config files and connection profiles;
- authorized database/report read surfaces.

Record each item as `found`, `absent`, `not installed`, `forbidden`, or `needs revalidation`.

## Test

No surface can be marked `absent` or `forbidden` until this depth checklist is attached to the Source Registry.
