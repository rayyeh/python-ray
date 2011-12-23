#!/bin/bash
echo "start NTP time"
gtacl -c "$(python ntp.py)"
gtacl -c "$(python ntp.py)"