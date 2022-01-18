# WebsiteMonitor for HA
[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]
Custom component for Home Assistant that monitors websites.
based on https://github.com/mvdwetering/websitechecker

Didn't make many changes, but am continuing to develop.

This is mostly to monitor my websites and other online services.
Based this off mvdwetering as thought it was great for me to learn custom components for Home Assistant.

OK - Websites must return a HTTP request with response code < 500
Down - No response code or response code 0
Problematic - Response code >= 500

### Install

### HACS

* Add this repository https://github.com/bmelim/websitemonitor to HACS
* Install the integration from within HACS

### Configuration

* Add `website_monitor:` to `configuration.yaml` and add some URLs to check
* Restart Home Assistant.

### Example config
```
websitemonitor:
  websites:
    - url: https://labrat.io
      name: Labrat.io
    - url: https://google.com
      name: Google
```
