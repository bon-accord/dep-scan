# Introduction

```bash
  ___            _____ _                    _
 / _ \          |_   _| |                  | |
/ /_\ \_ __  _ __ | | | |__  _ __ ___  __ _| |_
|  _  | '_ \| '_ \| | | '_ \| '__/ _ \/ _` | __|
| | | | |_) | |_) | | | | | | | |  __/ (_| | |_
\_| |_/ .__/| .__/\_/ |_| |_|_|  \___|\__,_|\__|
      | |   | |
      |_|   |_|
```

dep-scan is a fully open-source security audit tool for project dependencies based on known vulnerabilities and advisories. The output is fully compatible with [grafeas](https://github.com/grafeas/grafeas). The tool is ideal for CI environments with built-in build breaker logic.

**NOT READY**

The tool is a work-in-progress and is not ready for production use. Consider this as a preview for demonstration purposes. There are a number of unresolved problems:

- Large number of false positives due to overly jealous version matching (ignores any excludes :())
- in-ability to distinguish package names belonging to different groups (since the matching is purely based on names and versions!)

[![Docker Repository on Quay](https://quay.io/repository/appthreat/dep-scan/status "Docker Repository on Quay")](https://quay.io/repository/appthreat/dep-scan)

## Features

- Package vulnerability scanning is performed locally and is quite fast. No server is used!
- Configurable `cache` and `sync` functionality to manage local cache data
- Supports direct input from [sast-scan](https://github.com/AppThreat/sast-scan/)
- Automatic submission to grafeas server (Coming soon!)

## Usage

dep-scan is ideal for use with CI and also as a tool for local development.

### Customisation through environment variables

Following environment variables can be used to customise the behaviour.

- VULNDB_HOME - Directory to use for caching database. For docker based execution, this directory should get mounted as a volume from the host
- NVD_START_YEAR - Default: 2018. Supports upto 2002
- GITHUB_PAGE_COUNT - Default: 2. Supports upto 20

### Scanning projects locally (Python version)

```bash
pip install appthreat-depscan
```

This would install a command called `scan`. You can invoke this command directly with the various options.

```bash
scan --src /app --report_file /app/reports/depscan.json
```

### Scanning projects locally (Docker container)

`appthreat/dep-scan` or `quay.io/appthreat/dep-scan` container image can be used to perform the scan.

To scan with default settings

```bash
docker run --rm -v $PWD:/app appthreat/dep-scan scan --src /app --report_file /app/reports/depscan.json
```

To scan with custom environment variables based configuration

```bash
docker run --rm \
    -e VULNDB_HOME=/db \
    -e NVD_START_YEAR=2010 \
    -e GITHUB_PAGE_COUNT=5 \
    -e GITHUB_TOKEN=<token> \
    -v /tmp:/db \
    -v $PWD:/app appthreat/dep-scan scan --src /app --report_file /app/reports/depscan.json
```

In the above example, `/tmp` is mounted as `/db` into the container. This directory is then specified as `VULNDB_HOME` for caching the vulnerability information. This way the database can be cached and reused to improve performance.

## GitHub security advisory

To download security advisories from GitHub, a personal access token with the following scope is necessary.

- read:packages

```bash
export GITHUB_TOKEN="<PAT token>"
```

This environment variable is not required when dep-scan is executed via GitHub action.

## Alternatives

[Dependency Check](https://github.com/jeremylong/DependencyCheck) is considered to be the industry standard for open-source dependency scanning. After personally using this great product for a number of years I decided to write my own from scratch partly as a dedication to this project. By using a streaming database based on msgpack and using json schema, dep-scan is more performant than dependency check in CI environments. Plus with support for GitHub advisory source and grafeas report export and submission, dep-scan is on track to become a next-generation dependency audit tool

There are a number of other tools that piggy back on Sonatype [ossindex](https://ossindex.sonatype.org/). For some reason, I always felt uncomfortable letting a commercial company track the usage of various projects across the world. dep-scan is completely private and does no tracking!
