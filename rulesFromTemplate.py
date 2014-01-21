__author__ = 'nightwing'


from sys import argv

T = "Blah blah blah COMPID, blah blhah COMPID, COMPNAME"

C = [
    ["B1", "Boogie1"],
    ["B2", "Boogie2"],
    ["B3", "Boogie3"],
    ["B4", "Boogie4"],
]

S = "CNBC"


if __name__ == "__main__":
    print len(argv)
    if len(argv) != 4:
        print 'usage: python '+argv[0]+' <template_file_path> <companies_list_path>'

    else:
        print 'Starting Process'

        template_file = argv[1]
        companies_list = argv[2]
        source_name = argv[3]

        template = open(template_file, 'r').read()
        companies = map(lambda x: x.strip().split(";"), open(companies_list, 'r').readlines())

        for (ind, c) in enumerate(companies):
            fout = open("sources/%s%d.json"%(source_name, ind+1), 'w')
            print 'Writing to', fout.name
            content = template.replace("COMPID", c[1])
            fout.write(content.replace("COMPNAME", c[0]))
            fout.close()

        print 'Process complete'