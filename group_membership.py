#!/usr/bin/python

import argparse
import os

import googleapiclient.discovery

from auth import get_authenticated_http

DIRECTORY_SCOPE = 'https://www.googleapis.com/auth/admin.directory.group.readonly'

parser = argparse.ArgumentParser(
    description="Retrieve a user's group membership")
parser.add_argument('domain', help="The Groups for Business domain")
parser.add_argument('user_key', help="The user's email address or ID")

args = parser.parse_args()

directory_service = googleapiclient.discovery.build(
    'admin',
    'directory_v1',
    http=get_authenticated_http(DIRECTORY_SCOPE))

groups = directory_service.groups().list(
    domain=args.domain,
    userKey=args.user_key).execute()['groups']

for group in groups:
    print("{0[name]} ({0[email]})".format(group))
