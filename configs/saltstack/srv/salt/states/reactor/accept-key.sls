#
# Using kwargs due to
# https://github.com/saltstack/salt/issues/43017
#
{% if 'act' in data and data['act'] == 'pend' %}
minion_add:
  wheel.key.accept:
    - match: {{ data['id'] }}
{% endif %}

