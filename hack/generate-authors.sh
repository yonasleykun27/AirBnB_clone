#!/usr/bin/env bash
set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd)"
ROOTDIR="$(cd "${SCRIPTDIR}/.." >/dev/null && pwd)"

set -x

# see also ".mailmap" for how email addresses and names are deduplicated

cat << 'EOF' > "${ROOTDIR}/AUTHORS"
# This file lists all individuals having contributed content to the repository.
# For how it is generated, see `hack/generate-authors.sh`.
EOF
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf >> "${ROOTDIR}/AUTHORS"
