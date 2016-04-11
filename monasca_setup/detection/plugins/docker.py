# (C) Copyright 2015 Hewlett Packard Enterprise Development Company LP

import logging
import os

import yaml

import monasca_setup.agent_config
import monasca_setup.detection

log = logging.getLogger(__name__)


class Docker(monasca_setup.detection.Plugin):

    """Detect Docker daemons and setup configuration to monitor them.

    """

    def _detect(self):
        """Run detection, set self.available True if the service is detected.

        """
        if monasca_setup.detection.find_process_cmdline('docker') is not None:
            self.available = True


    def build_config(self):
        """Build the config and return.

        """
        log.info("\tWatching the named process.")
        return monasca_setup.detection.watch_process(
            ['docker'], 'docker', exact_match=False)

    def dependencies_installed(self):
        return True
