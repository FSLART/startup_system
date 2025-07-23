#!/bin/bash
source /opt/ros/humble/setup.bash
source /home/lart-tasha/Documents/repos/ros2_ws/install/setup.bash

echo "[STARTUP] A iniciar o sistema..."

# Ativar interface CAN
#echo "[CAN] A ativar a interface CAN..."
bash /home/lart-tasha/setup_can_usb.sh

# Lançar launch file
ros2 launch startup_system initialize_nodes.launch.py

