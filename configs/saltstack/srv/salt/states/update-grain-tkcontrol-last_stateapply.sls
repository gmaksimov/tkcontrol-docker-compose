update-grain-tkcontrol-last_stateapply:
  grains.present:
    - name: tkcontrol:last_stateapply
    - value: "{{ salt['cmd.run']('date +"%Y-%m-%d %H:%M:%S%z" -u') }}"
    - fire_event: custom/updated-tkcontrol-last_stateapply
