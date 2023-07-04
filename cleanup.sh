#!/bin/bash

echo "Performing Cleanup"
sudo find /components -name "*.pyc" -exec rm -f {} \;