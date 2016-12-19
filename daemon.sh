#!/bin/sh
set -efu

rfcomm=/dev/rfcomm1

turn_on() {
  echo -n a > "${rfcomm}"
}

turn_off() {
  echo -n b > "${rfcomm}"
}

autocontrol() {
  if [ "${temperature}" -lt "$min_temperature" ]; then
    turn_on
  else
    turn_off
  fi
}

while :; do
  temperature=`echo -n 't' | ./unbuf.py | awk '{ print $3 }'`
  min_temperature=`cat min_temperature`
  mode=`cat mode`
  sleep 2

  case "${mode}" in
    ON|on) turn_on;;
    OFF|off) turn_off;;
    *) autocontrol;;
  esac

  echo "Mode ${mode}. The temperature is ${temperature} C, minimal is ${min_temperature}"
  echo "${temperature}" > temperature
  sleep 5
done
