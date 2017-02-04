# IndustrialHack

## Objective

Find the GE-SRTP that are public and not secured correctly. Then find contact 
information for people using the non secure system. Then make list for future 
contact.

## How

There are a few different steps

1. Identify services with ports 18245 or 18246 open
2. Look for bytes /x01/x00... as a response (it is a GE-SRTP device)
3. Search ports for identifyable information
  * ensure that it is still running
  * check for other ips at the same location (up to 3 can be hosted on the same 
  device, if there is more than 3 then there are two devices)
  * check ports for identifyable services which include (for all ips):
   * ftp - 21
   * ssh - 22
   * telnet - 23
   * HTTP - 80
   * SSL/HTTPS - 443
4. Use this identifyable information to then look the person's contact 
information.
5. If no person can be found, then geo location can be used to attempt to 
identify the owner of the device.

## Implementation

Use python to search using apis such as Shodan and Censys.

