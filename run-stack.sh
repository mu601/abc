#!/bin/bash

set -eu


aws cloudformation deploy --template-file minhaz-bucket-stack.yml \
		--stack-name minhaz-bucket-stack --profile minhaz-profile