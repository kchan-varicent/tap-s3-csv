from voluptuous import Schema, Required, Optional

CONFIG_CONTRACT = Schema([{
    Required('name'): str,
    Required('pattern'): str,
    Required('key_properties'): [str],
    Optional('search_prefix'): str,
    Optional('date_overrides'): [str]
}])
