`statuspage`: Manage statuspage.io components & incidents from Cog
==================================================================

# TL;DR
    !statuspage:incident new -s investigating -i critical -c database -n "Denied logins" Increased errors from our primary database is causing new logins to fail. Our operations team is investigating.
    !statuspage:incident update -s resolved -n "Denied logins" A failing disk on our primary database host is the primary cause of this outage. We have failed over to our backup host while the drive is replaced. Logins have been restored and we continue to monitor the situation.

# Overview

The `statuspage` bundle exposes two commands, `component` and
`incident`, which allow you view statuspage.io components and
incidents as well as create and update 'realtime' incidents.

By default, anyone can execute the `statuspage:component` command
since its operation is read-only. Execution of the
`statuspage:incident` command requires the `statuspage:update` permission.

# Installing

    curl -O https://github.com/cog-bundles/statuspage/blob/master/config.yaml
    cogctl bundle install config.yaml

# Configuring

The `statuspage` bundle requires your statuspage.io page id and API
token. Relay's dynamic configuration feature is the easiest way to
make this happen. Simply create a directory named `statuspage` inside
Relay's dynamic configuration root directory. Then drop a file named
`config.yaml` in the newly created directory with the following
contents:

```yaml
---
page_id: <YOUR_PAGE_ID>
api_token: <YOUR_API_TOKEN>
```


# Building

To build the Docker image, simply run:

    $ make docker

Requires Python 3.5.x, pip, make, and Docker.
