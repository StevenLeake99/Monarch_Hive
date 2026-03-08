
#!/bin/bash
echo "starting tor service"
tor --HiddenServiceDir ./tor_service --HiddenServicePort 80 127.0.0.1:8080
