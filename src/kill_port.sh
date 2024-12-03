#!/bin/bash
PORT=5000
PID=$(lsof -t -i:$PORT)
if [ ! -z "$PID" ]; then
    echo "Killing process $PID on port $PORT"
    kill -9 $PID
else
    echo "No process found on port $PORT"
fi

