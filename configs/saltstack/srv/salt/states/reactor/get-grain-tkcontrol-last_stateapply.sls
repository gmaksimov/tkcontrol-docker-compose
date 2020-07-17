get-grain-tkcontrol-last_stateapply:
  local.grains.get:
    - tgt: {{ data['id'] }}
    - arg:
      - "tkcontrol:last_stateapply"
