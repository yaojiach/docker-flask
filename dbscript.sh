#!/bin/bash
psql << EOF
    create database jwt;
    create user dev with password '12345';
    grant all privileges on jwt to dev;
EOF

psql postgresql://dev:12345@localhost:5432/jwt -a -f dbscript.sql