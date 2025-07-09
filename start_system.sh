#!/bin/bash
source /opt/ros/humble/setup.bash
source ~/lart/ros2_ws/src/install/setup.bash

echo "[STARTUP] A iniciar o sistema..."

# Ativar interface CAN
#echo "[CAN] A ativar a interface CAN..."
#bash setup_can_usb.sh

# Lançar launch file
ros2 launch startup initialize_nodes.launch.py

