tshark -r capture.pcap -Y 'http.response and !(http contains "FAILED")' -T fields -e http.response_for.uri > paths.txt
