# dt_hijack

1. ./start_joystick_container.sh
2. ./start_hj_container.sh
3. (in hj_container) cd /home/..../dt_hijack && python3 duckie_hijacker.py
4. ./exec_hj_container.sh
5. (in second hj_container) cd /home/..../dt_hijack && python3 tmp_hijack_pub.py



## How to move
in tmp_hijack_pub, publish

1 => forward
2 => backward
3 => right
4 => left
