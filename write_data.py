import bz2file
import json
import os
import process_data


years = ['2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017']
months = ['01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12']

test_years = ['2009']
test_months = ['01', '02', '12']


for year in test_years:
    DATA_DIR = os.path.join("D:\\", "reddit", "reddit_data", str(year))
    for month in test_months:
        reddit_json = []
        filename = "RC_" + str(year) + "-" + str(month) + ".bz2"
        print(DATA_DIR + "\\" + filename)
        print("Accessing " + DATA_DIR + "\\" + filename + "...")
        try:
            with bz2file.open(DATA_DIR + "\\" + filename, 'r',
                              compresslevel=9,
                              encoding=None,
                              errors=None,
                              newline=None) as f:
                for i, line in enumerate(f):
                    data = json.loads(line)
                    reddit_json.append(data)
                print("Successfully imported data from "+month+"."+year)
                print("Processing data...")
                try:
                    #process_data.remove_keys(reddit_json)
                    #process_data.get_date(reddit_json)
                    #process_data.rename_keys(reddit_json)
                    process_data.get_comments(reddit_json)
                    print("Successfully processed the data!")
                except:
                    print("Error in one of the data processing functions! Check proces_data.py")

                print("Writing data to data" + year + month + ".txt")
                try:
                    with open("data" + year + "-" + month + ".txt", "w") as json_f:
                        # for elem in reddit_json:
                        #    print("An instance (dictionary) added to the data set:\n", elem)
                        json.dump(process_data.get_comments(reddit_json), json_f)
                        json_f.close()
                        print("Successfully wrote data!")
                except:
                    print("Error in writing data")
                f.close()
        except OSError:
            print("Error loading " + DATA_DIR + "\\" + filename)

