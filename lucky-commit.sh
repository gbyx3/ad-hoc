#!/usr/bin/env bash
# Generate commit message to be lucky
# Based on a X-thread "demanding" a commit hash with a specific prefix

function is_hex() {
    if [[ $1 =~ ^[0-9a-fA-F]+$ ]]; then
        return 0
    else
        return 1
    fi
}

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 '<commit_message>'"
    exit 1
fi

MATCH="ea"
if ! is_hex $MATCH; then
    echo "The match string is not a valid hex string"
    echo "Converting to hex string"
    MATCH=$(echo -n $MATCH |xxd -p)
fi

LENGTH=${#MATCH}
MESSAGE=$1
while true; do
    commit_hash=$(sha1sum <<< "$MESSAGE" | cut -c1-$LENGTH)
    if [[ $commit_hash == $MATCH ]]; then
        echo "Lucky commit: $MESSAGE |<- "
        exit 0
    fi
    MESSAGE="$MESSAGE "
    echo "$commit_hash"
done
