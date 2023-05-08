import csv
import ipaddress

# Open the input CSV file
with open('input.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader) # Skip the header row

    # Open the output CSV file and write the header row
    with open('output.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'First IP', 'Last IP'])

        # Loop over each row in the input CSV file
        for row in reader:
            cidr = row[0]
            network_type = row[1]
            name = row[2]

            # Calculate the first and last IP addresses in the CIDR range
            ip_network = ipaddress.ip_network(cidr)
            first_ip = str(ip_network.network_address)
            last_ip = str(ip_network.broadcast_address)

            # Combine the network type and name into a single column
            label = '-- ' + network_type + ' -- ' + name + ' (' + cidr.replace('/', '_') + ')'

            # Write the results to the output CSV file
            writer.writerow([label, first_ip, last_ip])