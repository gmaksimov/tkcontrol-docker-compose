base:

  #'*':
  #  - custom.sls

  '*':
    # Update last_stateapply datetime on state.apply
    - update-grain-tkcontrol-last_stateapply
