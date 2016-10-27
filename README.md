Manage statuspage.io incidents from Cog
=======================================

# TL;DR

    !statuspage:incident new -s investigating -i critical -c database -n "Denied logins" Our database is sick
    !statuspage:incident update -s resolved -n "Denied logins" It got better

# Overview

The `statuspage` bundle exposes two commands, `component` and
`incident`, which allow you view statuspage.io components and
incidents as well as create and update 'realtime' incidents.

By default, anyone can execute the `statuspage:component` command
since its operation is read-only. Execution of the
`statuspage:incident` command requires the `statuspage:update` permission.

# Installing

In chat:

```
@cog bundle install statuspage
```

From the command line:

```
cogctl bundle install statuspage
```

# Configuring

The `statuspage` bundle requires your statuspage.io page id and API
token. You can set these variables with Cog's dynamic config feature:

```bash
echo 'page_id: <YOUR_PAGE_ID>' >> config.yaml
echo 'api_token: <YOUR_PAGE_ID>' >> config.yaml
cogctl dynamic-config create statuspage config.yaml
```

# Building

To build the Docker image, simply run:

    $ make docker

Requires Python 3.5.x, pip, make, and Docker.
