#!/bin/bash
set -e

# Setup catkin workspace
source "/opt/ros/$ROS_DISTRO/setup.sh" && catkin_make
source devel/setup.sh

# Setup ROS environment
echo "source \"/opt/ros/$ROS_DISTRO/setup.sh\"" >> /etc/bash.bashrc
echo "source /workspace/devel/setup.sh" >> /etc/bash.bashrc

# Setup executable files
chmod +x src/scripts/launch_dm_intent.py

# Download model files
sudo apt-get install unzip
sudo apt-get install curl
echo "Model Download PATH : "pwd
FILEID='1UnXusiOMAaoNnLy245QhQVSqlbRxetbB'
FILENAME='hyu_intent.zip'
curl -c /tmp/cookie -s -L "https://drive.google.com/uc?export=download&id=${FILEID}" > /dev/null
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' /tmp/cookie`&id="${FILEID} -o ${FILENAME}
rm /tmp/cookie
rm -rf authkey/
rm -rf ckpt/
unzip $FILENAME
mv hyu_intent/authkey/configuration.json src/configuration.json
mv hyu_intent/authkey src/
mv hyu_intent/ckpt src/
rm -r hyu_intent
rm $FILENAME
echo "Modelfile Download Complete!!"

# Execute CMD
exec "$@"

