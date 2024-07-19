from io import BytesIO, StringIO

def csv_to_tsv(file):
    output = BytesIO()
    with file as f:
        for line in f:
            line=line.decode('utf-8')
            line = line.replace(',', '\t')
            print(line)
            output.write(line.encode('utf-8')) #write to output file
    output.seek(0) #set the pointer to the beginning of the file
    return output


def tsv_to_csv(file):
    output = BytesIO()
    with file as f:
        for line in f:
            line=line.decode('utf-8')
            line = line.replace('\t', ',')
            print(line)
            output.write(line.encode('utf-8')) #write to output file
    output.seek(0) #set the pointer to the beginning of the file
    return output