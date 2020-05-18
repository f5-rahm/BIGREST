# External Imports
# Import only with 'import package',
# it will make explicity in the code where it came from.

# Turns all annotations into string literals.
# This is one exception to the external import rule.
from __future__ import annotations


class RESTObject():
    """Represent a object created from a response to an iControl REST call."""

    def __init__(self, properties: dict) -> RESTObject:
        self.properties = properties

    def asdict(self) -> dict:
        # iControl REST only accepts enabled=True or disabled=True
        if 'enabled' in self.properties:
            if self.properties['enabled'] is True:
                self.properties.pop('enabled')
                self.properties['disabled'] = True
        if 'disabled' in self.properties:
            if self.properties['disabled'] is True:
                self.properties.pop('enabled')
                self.properties['enabled'] = True
        return self.properties