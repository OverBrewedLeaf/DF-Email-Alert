

import sys
import time
import email
import socket
import imaplib
import smtplib
import paramiko
import re
from datetime import datetime, timedelta
from email.header import Header
from email.utils import parseaddr, formataddr

DEBUG = True
PRINT_SSH_CONSOLE = False

SELF_TEST = True
TEST_ENV = True