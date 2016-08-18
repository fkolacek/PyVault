#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: 
# Author: fkolacek@redhat.com
# Version: 0.1a

import sys
import os
import argparse
import json
from pprint import pprint

def printMsg(errorMessage):
  print "[*] %s" % errorMessage

def printError(errorMessage, errorCode):
  print "[!] %s" % errorMessage
  exit(errorCode)

class cParser(argparse.ArgumentParser):
  def error(self, message):
    self.print_help()
    exit(2)

class Store(object):

  filename = None
  content = {}

  def __init__(self, filename):
    self.filename = filename

    if not os.path.exists(self.filename):
      printMsg("Vault %s does not exist, creating one." % self.filename)
      self.saveFile()
    else:
      self.loadFile()

  def write(self, key, val):
    self.checkKey(key)

    obj = self.content
    indexes = key.split('/')[1:]
    indexes_done = []
    for index in indexes[:-1]:
      if not isinstance(obj, dict):
        raise Exception("Entry /%s already exists, delete it first!" % '/'.join(indexes_done))

      if not index in obj:
        obj[index] = {}

      obj = obj[index]
      indexes_done.append(index)

    if not isinstance(obj, dict):
      raise Exception("Entry /%s already exists, delete it first!" % '/'.join(indexes_done))

    obj[indexes[-1]] = val

    self.saveFile()

  def read(self, key):
    self.checkKey(key)

    obj = self.content

    if key == '/':
      print obj
    else:
      indexes = key.split('/')[1:]

      for index in indexes[:-1]:
        if index not in obj:
          exit(2)

        obj = obj[index]

      if indexes[-1] not in obj:
        exit(2)

      print obj[indexes[-1]]

  def checkKey(self, key):
    if not key.startswith('/'):
      raise Exception('Invalid key (should start with /)')

    if key.endswith('/') and key != '/':
      raise Exception('Invalid key (should not end with /)')

  def loadFile(self):
    with open(self.filename, 'r') as f:
      self.content = json.load(f)
    f.closed

  def saveFile(self):
    with open(self.filename, 'w') as f:
      json.dump(self.content, f)
    f.closed

class Vault(object):

  description = "vault.py - Custom vault (fkolacek@redhat.com)"
  store = None

  def __init__(self):
    parser = cParser(
      description=self.description, add_help=False, usage='''vault.py <command>

Available commands are:
  init     Initialize specified vault
  read     Read specific entry
  write    Write specific entry
  delete   Delete specific entry''')

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

    self.store = Store(args.filename[1])

  def write(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py write <filename> <key> <value>")
    parser.add_argument("filename", nargs=2, help="Path to specified vault")
    parser.add_argument("key", nargs=1, help="Entry key")
    parser.add_argument("value", nargs=1, help="Entry value")
    args = parser.parse_args()

    self.store = Store(args.filename[1])
    self.store.write(args.key[0], args.value[0])

  def read(self):
    parser = cParser(description=self.description, add_help=False, usage="vault.py read <filename> <key>")
    parser.add_argument("filename", nargs=2, help="Path to specified vault")
    parser.add_argument("key", nargs=1, help="Entry key")
    args = parser.parse_args()

    self.store = Store(args.filename[1])
    self.store.read(args.key[0])

  def delete(self):
    pass

if __name__ == '__main__':

  try:
    import gnupg

    Vault()
  except ImportError:
    printError("Required module 'gnupg' not found. Please install it by running 'pip install python-gnupg' as root.", 1)
  except Exception, err:
    printError('%s' % str(err), 2)

