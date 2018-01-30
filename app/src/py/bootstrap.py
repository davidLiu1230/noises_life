#!/usr/bin/env python
import logging, os

from constants import LOG_FILENAME, LOG_BASE_DIR

def bootstrap():
  """
  Returns: bool - True if bootstrap finished without error, False otherwise
  """
  filename = os.path.join(LOG_BASE_DIR, LOG_FILENAME)
  logging.basicConfig(
  	  filename=filename,
  	  filemode='a+',
  	  level=logging.INFO,
  	  format='%(asctime)s %(message)s')

  return True
