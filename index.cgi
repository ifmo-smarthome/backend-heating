#!/bin/bash -efu

echo 'Content-Type: application/json'
echo ''

exec 2>&1

json="`cat`"

action="`echo "$json" | jq -r ".action"`"

case "$action" in
  'getTemperature')
    temperature=`cat temperature`
    if [ ! -z "${temperature}" ]; then
      printf '{ "success": true, "result": { "temperature": %d } }' "${temperature}"
    else
      printf '{ "success": false, "error": "No daemon started" }'
    fi
    ;;
  'changeBatteryMode')
    mode="`echo "$json" | jq -r ".parameters.mode"`"
    echo "${mode}" > mode
    printf '{ "success": true, "result": { "mode": "%s" } }' "${mode}"
    ;;
  'changeTemperatureLimit')
    limit="`echo "$json" | jq -r ".parameters.limit"`"
    echo "$limit" > min_temperature
    printf '{ "success": true, "result": { "limit": %d } }' "${limit}"
    ;;
  *)
    printf '{ "success": false, "error": "No \"%s\" exists" }' "${action}"
    ;;
esac

echo ''
