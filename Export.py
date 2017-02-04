"""This module will handle exporting data from the filter to a csv file"""
import Location

def output_data(ips, filtered_data, output, filename):
    """This will output data in the following format (csv)
        ip\t location\t name\t email\t phone\t threat
        
       outputs is a dict which has each column as a key and booleans as values
       
       the ips are the ips used
       
       """
    final = ""
    if output['ip']:
        final += "ip\t "
    if output['location']:
        final += "location\t "
    if output['name']:
        final += "name\t "
    if output['email']:
        final += "email\t "
    if output['phone']:
        final += "phone\t "
    if output['address']:
        final += 'address\t '
    if output['threat']:
        final += "threat\n"
    for ip in ips:
        if filtered_data[ip]:
            for data_set in filtered_data[ip]:
                if output['ip']:
                    final += ip + '\t '
                if output['location']:
                    final += str(Location.find_location(ip)) + '\t '
                if output['name']:
                    final += data_set['name'] + '\t '
                if output['email']:
                    if data_set['email']:
                        final += str([email['value'] for email in data_set['email']]) + '\t '
                    else:
                        final += "[]\t "
                if output['phone']:
                    if data_set['phone']:
                        final += str([phone['value'] for phone in data_set['phone']]) + '\t '
                    else:
                        final += "[]\t "
                if output['address']:
                    if data_set['address']:
                        final += str([addr['value'] for addr in data_set['address']]) + '\t '
                    else:
                        final += "[]\t "
                if output['threat']:
                    final += "High"
                final += "\n"
        else:
            if output['ip']:
                final += ip + "\t "
            if output['location']:
                final += "None\t "
            if output['name']:
                final += "None\t "
            if output['email']:
                final += "[]\t "
            if output['phone']:
                final += "[]\t "
            if output['address']:
                final += '[]\t '
            if output['threat']:
                final += "Unknown"
            final += '\n'  
    out_file = open(filename, 'w')
    out_file.write(final)
    out_file.close()
        
if __name__ == "__main__":
    import webreader
    ips = webreader.get_ips_from_file("ips.csv")
    import IpFilter
    data = IpFilter.get_all_owner_info(ips)
    data = IpFilter.filter_blacklist_email_domains(data)
    output_data(ips, data, {'ip':True, 'location':True, 'name':True, 'email':True, 'phone':True, 'address':True, 'threat':True}, 'out2.csv')

