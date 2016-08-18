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

class Store:

  def __init__(self, filename):
    pass

  def set(self, key, val):
    pass

  def get(self, key):
    pass

class Vault(object):

  description = "vault.py - Custom vault (fkolacek@redhat.com)"
  store = None

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
    parser.add_argument("filename", nargs=2, help="Path to specified vault")
    args = parser.parse_args()

    try:
      self.store = Store(args.filename[1])
    except:
      pass

  def set(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py set <filename> <key> <value>")
    parser.add_argument("filename", nargs=2, help="Path to specified vault")
    parser.add_argument("key", nargs=1, help="Entry key")
    parser.add_argument("value", nargs=1, help="Entry value")
    args = parser.parse_args()

    try:
      self.store = Store(args.filename[1])
      self.store.set(args.key[0], args.value[0])
    except:
      pass

  def get(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py get <filename> <key>")
    parser.add_argument("filename", nargs=2, help="Path to specified vault")
    parser.add_argument("key", nargs=1, help="Entry key")
    args = parser.parse_args()

    try:
      self.store = Store(args.filename[1])
      self.store.get(args.key[0])
    except:
      pass

if __name__ == '__main__':
  Vault()
