cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
lgraph_server -d stop
rm -rf ./lgraph_db
rm -rf ./log
rm -rf ./core.*