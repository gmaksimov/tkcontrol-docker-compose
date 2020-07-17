highstate_first_run:
  local.state.apply:
    - tgt: {{ data['id'] }}
