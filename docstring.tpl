{{! Google Docstring Template }}
{{summaryPlaceholder}}

{{extendedSummaryPlaceholder}}

{{#parametersExist}}
Args:
{{#args}}
    {{var}}: {{descriptionPlaceholder}}
{{/args}}
{{#kwargs}}
    {{var}}: {{descriptionPlaceholder}}. Defaults to {{&default}}.
{{/kwargs}}
{{/parametersExist}}

{{#exceptionsExist}}
Raises:
{{#exceptions}}
    {{type}}: {{descriptionPlaceholder}}
{{/exceptions}}
{{/exceptionsExist}}

{{#returnsExist}}
Returns:
{{#returns}}
    {{descriptionPlaceholder}}
{{/returns}}
{{/returnsExist}}

{{#yieldsExist}}
Yields:
{{#yields}}
    {{descriptionPlaceholder}}
{{/yields}}
{{/yieldsExist}}
