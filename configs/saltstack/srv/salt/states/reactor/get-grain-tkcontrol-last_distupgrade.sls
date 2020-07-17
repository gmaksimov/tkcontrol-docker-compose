get-grain-tkcontrol-last_distupgrade:
  local.grains.get:
    - tgt: {{ data['id'] }}
    - arg:
      - "tkcontrol:last_distupgrade"
