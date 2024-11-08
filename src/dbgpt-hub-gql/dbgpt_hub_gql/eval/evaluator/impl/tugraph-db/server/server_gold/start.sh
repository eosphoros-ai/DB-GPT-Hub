cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
lgraph_server -d stop
lgraph_server -c ./lgraph_standalone.json -d start