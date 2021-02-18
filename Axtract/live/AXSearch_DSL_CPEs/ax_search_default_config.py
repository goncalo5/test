from ax.utils.ordereddict import OrderedDict

view_fields = OrderedDict()

view_fields['cpe_separator'] = {
    'css_class': 'center',
    'field_type': 'separator',
    'target': 'search',
    'text': '-- CPE fields --',
    'unselectable': 1
}

view_fields['_id'] = {
    'css_class': 'center',
    'field_type': 'input',
    'format': 'ext:ax_search_formatter.generate_cpe_details',
    'format_params': 'AXCustomerSupportPortal',
    'csv_format': 'ext:ax_search_formatter.csv_format',
    'selected': 1,
    'text': 'CPE ID',
    'unselectable': 1}

view_fields['mode'] = {
    'css_class': 'center',
    'field_type': 'input',
    'selected': 1,
    'text': 'Mode'
}

view_fields['lastmsg'] = {
    'css_class': 'center',
    'field_type': 'date',
    'format': 'ext:ax_search_formatter.convert_datetime_ts_to_str',
    'selected': 1,
    'text': 'Last message'
}

view_fields['pii_set'] = {
    'css_class': 'center',
    'field_type': 'input',
    'selected': 1,
    'text': 'PII'
}

view_fields['next_forward'] = {
    'css_class': 'center validate[required,custom[number]]',
    'field_type': 'numeric',
    'format': 'ext:ax_search_formatter.convert_datetime_ts_to_str',
    'selected': 1,
    'text': 'Next Forward'
}

view_fields['last_update'] = {
    'css_class': 'center',
    'field_type': 'date',
    'format': 'ext:ax_search_formatter.convert_datetime_ts_to_str',
    'text': 'Last update',
    'selected': 1
}

view_fields['mode_props.ax.dsl.uptime'] = {
    'css_class': 'center',
    'field_type': 'date',
    'format': 'ext:ax_search_formatter.convert_float_ts_to_str',
    'text': 'Uptime',
    'selected': 1
}

return {
    'view_fields': view_fields,
    'store_type': 'cpe',
    'report_name': '',
    'implicit_condition': ''
}
