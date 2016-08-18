#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: 
# Author: fkolacek@redhat.com
# Version: 0.1a

import sys
import os
import argparse
from pprint import pprint

class cParser(argparse.ArgumentParser):
  def error(self, message):
    self.print_help()
    exit(2)

class Vault(object):

  description = "vault.py - Custom vault (fkolacek@redhat.com)"

  def __init__(self):
    parser = cParser(
      description=self.description, add_help=False, usage='''vault.py <command>

Available commands are:
  init     Initialize specified vault
  set      Set specific entry
  get      Get specific entry''')

    parser.add_argument("command", help="Subcommand to run")

    args = parser.parse_args(sys.argv[1:2])

    if not hasattr(self, args.command):
      parser.print_help()
      exit(1)

    getattr(self, args.command)()

  def init(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py init <filename>")
    parser.add_argument("name", nargs=2, help="Name of the vault")
    args = parser.parse_args()

    name = args.name[1]

  def set(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py set <name> <value>")
    parser.add_argument("name", nargs=2, help="Entry name")
    parser.add_argument("value", nargs=1, help="Entry value")
    args = parser.parse_args()

    name = args.name[1]
    value = args.value[0]

  def get(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py get <name>")
    parser.add_argument("name", nargs=2, help="Name of the vault")
    args = parser.parse_args()

    name = args.name[1]

if __name__ == '__main__':
  Vault()
