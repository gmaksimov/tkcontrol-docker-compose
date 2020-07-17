apt-update:
  cmd.run:
    - name: apt-get update

apt-distupgrade:
  cmd.run:
    - name: apt-get dist-upgrade -y

update-grain-tkcontrol-last_distupgrade:
  grains.present:
    - name: tkcontrol:last_distupgrade
    - value: "{{ salt['cmd.run']('date +"%Y-%m-%d %H:%M:%S%z" -u') }}"
    - fire_event: custom/updated-tkcontrol-last_distupgrade
