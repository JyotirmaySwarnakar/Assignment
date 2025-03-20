
#Q4:Write a Bash script that monitors CPU and memory usage every 5 seconds and logs the data into a file.

!/bin/bash

while true
do
    cpu=$(top -bn1 | grep '%Cpu' | awk -F, '{print $4}' | awk '{print 100 - $1}')
    mem=$(free -m | grep Mem | awk '{print $3}')
    echo "$(date) CPU: $cpu% Mem: $mem MB" >> usage.log
    sleep 5
done

#Q6:Write a Bash script that finds and kills all processes consuming more than 80% CPU usage.

!/bin/bash

ps aux | awk '$3 > 80 {print $2}' | while read pid
do
    kill $pid
done

