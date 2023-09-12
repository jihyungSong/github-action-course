#!/bin/sh

mkdir $HOME/secrets

gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output $HOME/secrets/my_secret.json my_secret.json.gpg