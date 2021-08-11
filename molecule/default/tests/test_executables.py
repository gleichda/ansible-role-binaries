import os
import stat

binaries = [
    "btm",
    "bat",
    "dyff",
    "helm",
    "istioctl",
    "kind",
    "yq"
]

def test_binaries_exist(host):
    home = host.user("root").home
    for bin in binaries:
        filepath = os.path.join(home, ".local/bin", bin)
        assert host.file(filepath).exists
        assert host.file(filepath).mode == 0o755
