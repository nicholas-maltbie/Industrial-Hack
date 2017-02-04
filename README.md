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

### Step by step

1. This will probably use Shoden and export a list of ips that another module 
could use. These ips will all have the ports specified open (in this calse, 18245 
and 18246)

2. This is already taken care of by Shoden, although, if another attempt was 
made to use another search engine, this would then export a list of ips.

3. This takes a list of ips as an input. Then, this will search for identifyable 
information. This will be done using Censys.

  1. First, check for other ips at the same location. (this could be done with 
  a hash map and maping by location).
  
  2. Take the groups of ips with the same location. Check the person identifyed 
  at this location by one of the open services. The output is the list of names.
  
  3. If no person name can be found use a company name if possible.
  
  4. This will output a list of names.
  
4. Take this list of names and attempt to find contact info. This will also 
filter out large companies who would not own an industrial device such as 
phone companies.

5. If no contact info could be found, take the ips and then do a geo location 
search with some method.

### Human Example

First, we visited Shoden and used the GE-SRTP filter and US location. (1 and 2)

We then took the ips from this search and looked at open ports. (3)

We took these ports and ips and looked at censys to find any indentifyable 
information for a person or company. Filtering for cell phone companies. (4)

For the ones that a contact could not be found, we then searched for geo 
location using tools like traceroute and online services like google maps. (5)

### Next steps

Attempt to automate the Human Example

